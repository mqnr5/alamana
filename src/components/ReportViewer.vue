<template>
  <div class="report-viewer">
    <h1>📄 عارض التقارير</h1>

    <div class="report-actions">
      <label class="upload-label">
        📤 تحميل تقرير
        <input type="file" accept="application/pdf" @change="onFileChange" hidden />
      </label>
      <button v-if="pdfUrl" class="print-btn" @click="printPdf">🖨️ طباعة</button>
    </div>

    <div ref="notice" class="notice"></div>

    <transition name="fade">
      <div class="report-content" v-if="pdfUrl">
        <iframe :src="pageUrl()" frameborder="0" class="pdf-frame"></iframe>
      </div>
    </transition>

    <transition name="slide-fade">
      <div class="pagination" v-if="pdfUrl">
        <button @click="prevPage" :disabled="currentPage === 1">⬅️ السابق</button>
        <span>صفحة {{ currentPage }} من {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">التالي ➡️</button>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'ReportViewer',
  data() {
    return {
      pdfUrl: null,
      currentPage: 1,
      totalPages: 1,
      pdfFile: null,
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      if (file && file.type === "application/pdf") {
        this.pdfFile = file;
        this.pdfUrl = URL.createObjectURL(file);
        this.currentPage = 1;
        this.loadPdfPages(this.pdfUrl);
      } else {
        this.pdfUrl = null;
        this.totalPages = 1;
      }
    },
    async loadPdfPages(url) {
            const { PDFDocument } = await import('pdf-lib');
            const response = await fetch(url);
            const arrayBuffer = await response.arrayBuffer();
            const pdfDoc = await PDFDocument.load(arrayBuffer);
            pdfDoc.currentPage = this.currentPage;
            this.totalPages = pdfDoc.getPageCount();
    },
    pageUrl() {
      if (!this.pdfUrl) return '';
      return `${this.pdfUrl}#page=${this.currentPage}`;
    },
    prevPage() {
      if (this.currentPage > 1) this.currentPage--;
    },
    nextPage() {
      if (this.currentPage < this.totalPages) this.currentPage++;
    },
    restoreLastFile() {
    },
    printPdf() {
      const win = window.open(this.pageUrl(), '_blank');
      if (win) win.print();
    }
  },
  mounted() {
    this.restoreLastFile();
  }
};
</script>

<style scoped>
.report-viewer {
  padding: 25px;
  background: linear-gradient(145deg, #fafafa, #eaeaea);
  border-radius: 20px;
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.08);
  font-family: 'Tajawal', sans-serif;
  color: #2e2e2e;
  direction: rtl;
  text-align: center;
}

h1 {
  font-size: 26px;
  color: #3b3b99;
  margin-bottom: 20px;
}

.upload-label {
  display: inline-block;
  background-color: #4e5174;
  color: white;
  padding: 10px 20px;
  border-radius: 12px;
  cursor: pointer;
  font-weight: bold;
  margin: 0 10px;
  transition: background 0.3s;
}
.upload-label:hover {
  background-color: #6b6fa1;
}

.print-btn {
  background-color: #a40033;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-weight: bold;
  margin-top: 10px;
  transition: background-color 0.3s ease;
}
.print-btn:hover {
  background-color: #6c0024;
}

.notice {
  margin-top: 15px;
  font-size: 14px;
  color: #555;
  font-style: italic;
}

.report-content {
  margin-top: 25px;
}
.pdf-frame {
  width: 100%;
  height: 600px;
  border-radius: 12px;
  border: 2px solid #dedede;
  transition: all 0.3s ease-in-out;
}

.pagination {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
  align-items: center;
  flex-wrap: wrap;
}
.pagination button {
  background-color: #a40033;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 12px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
}
.pagination button:hover {
  background-color: #6c0024;
}
.pagination button:disabled {
  background-color: #c2c2c2;
  cursor: not-allowed;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all 0.4s ease;
}
.slide-fade-enter-from {
  transform: translateY(15px);
  opacity: 0;
}
</style>
