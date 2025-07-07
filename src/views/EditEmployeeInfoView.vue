<script>
import EditEmpInfo from '@/components/EditEmpInfo.vue'
export default {
    name: 'EditEmpInfoView',
    props: {
        userId: {
            type: Number,
            required: true
        }
    },
    components: {
        EditEmpInfo
    }
}
</script>
<template>
    <EditEmpInfo :userId="userId" />
</template>
<style scoped>

</style>
