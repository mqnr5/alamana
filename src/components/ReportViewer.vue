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
            const pdfjsLib = await import('pdfjs-dist/build/pdf');
            pdfjsLib.GlobalWorkerOptions.workerSrc = 
                'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.2.67/pdf.worker.min.js';
            const pdf = await pdfjsLib.getDocument(url).promise;
            this.totalPages = pdf.numPages;
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
        }
    }
}
</script>
<template>
    <div class="report-viewer">
        <h1>عارض التقارير</h1>
        <div class="report-actions">
            <input type="file" accept="application/pdf" @change="onFileChange" />
        </div>
        <div class="report-content" v-if="pdfUrl">
            <iframe :src="pageUrl()" frameborder="0"></iframe>
        </div>
        <div class="pagination" v-if="pdfUrl">
            <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
            <span>Page {{ currentPage }} of {{ totalPages }}</span>
            <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
        </div>
    </div>
</template>
<style scoped>
.report-viewer {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
h1 {
    justify-self: center;
}
.report-content {
    margin: 20px 0;
}
.report-content iframe {
    width: 100%;
    height: 600px;
    border: none;
}
.pagination {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}
.pagination button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.pagination button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}
.report-actions {
    margin-top: 20px;
}
</style>
