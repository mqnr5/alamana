import axios from "axios";

const BASE_URL = 'https://3zpk28dv-8000.inc1.devtunnels.ms';

// ==================== GET ====================
export async function get_users() {
    const response = await axios.get(`${BASE_URL}/users`)
    if (!response.data) {
        alert('Failed to fetch data from the database')
        return 1
    } else {
        return response.data.users
    }
}

export async function get_departments() {
    const response = await axios.get(`${BASE_URL}/departments`);
    return response.data.departments
}

export async function get_tasks() {
    const response = await axios.get(`${BASE_URL}/tasks`);
    return response.data.tasks
}

export async function get_missions(user_id) {
    const response = await axios.get(`${BASE_URL}/missions/${user_id}`);
    return response.data.missions
}

export async function get_notifications(user_id) {
    const response = await axios.get(`${BASE_URL}/notifications/${user_id}`);
    return response.data.notifications
}

export async function get_hurryup_alerts() {
    const response = await axios.get(`${BASE_URL}/hurryup_alerts`);
    return response.data.hurryup_alerts
}

export async function get_review_requests() {
    const response = await axios.get(`${BASE_URL}/review_requests`);
    return response.data.review_requests
}

export async function get_user_by_id(user_id) {
    const response = await axios.get(`${BASE_URL}/users/${user_id}`)
    if (!response.data) {
        alert('Failed to fetch data from the database')
        return 1
    } else {
        return response.data.user
    }
}

export async function get_department_by_id(department_id) {
    const response = await axios.get(`${BASE_URL}/departments/${department_id}`);
    if (!response.data) {
        alert('Failed to fetch data from the database');
        return 1;
    } else {
        return response.data.department
    }
}

// ==================== POST ====================
export async function add_user(user) {
    const response = await axios.post(`${BASE_URL}/users`, user)
    if (!response.data) {
        alert('Failed to add user to the database')
        return 1
    } else {
        return response.data
    }
}

export async function add_department(department) {
    const response = await axios.post(`${BASE_URL}/departments`, department);
    return response.data;
}

export async function add_task(task) {
    const response = await axios.post(`${BASE_URL}/tasks`, task);
    return response.data;
}

export async function add_mission(mission) {
    const response = await axios.post(`${BASE_URL}/missions`, mission);
    return response.data;
}

export async function add_hurryup_alert(alert) {
    const response = await axios.post(`${BASE_URL}/hurryup_alerts`, alert);
    return response.data;
}

export async function add_review_request(request) {
    const response = await axios.post(`${BASE_URL}/review_requests`, request);
    return response.data;
}

// ==================== UPDATE ====================
export async function update_user(user_id, user) {
    const response = await axios.put(`${BASE_URL}/users/${user_id}`, user);
    return response.data;
}

export async function update_department(department_id, department) {
    const response = await axios.put(`${BASE_URL}/departments/${department_id}`, department);
    return response.data;
}

export async function update_task(task_id, task) {
    const response = await axios.put(`${BASE_URL}/tasks/${task_id}`, task);
    return response.data;
}

export async function update_mission(mission_id, mission) {
    const response = await axios.put(`${BASE_URL}/missions/${mission_id}`, mission);
    return response.data;
}

export async function update_hurryup_alert(alert_id, alert) {
    const response = await axios.put(`${BASE_URL}/hurryup_alerts/${alert_id}`, alert);
    return response.data;
}

export async function update_review_request(request_id, request) {
    const response = await axios.put(`${BASE_URL}/review_requests/${request_id}`, request);
    return response.data;
}

// ==================== DELETE ====================
export async function delete_user(user_id) {
    const response = await axios.delete(`${BASE_URL}/users/${user_id}`);
    return response.data;
}

export async function delete_department(department_id) {
    const response = await axios.delete(`${BASE_URL}/departments/${department_id}`);
    return response.data;
}

export async function delete_task(task_id) {
    const response = await axios.delete(`${BASE_URL}/tasks/${task_id}`);
    return response.data;
}

export async function delete_mission(mission_id) {
    const response = await axios.delete(`${BASE_URL}/missions/${mission_id}`);
    return response.data;
}

export async function delete_hurryup_alert(alert_id) {
    const response = await axios.delete(`${BASE_URL}/hurryup_alerts/${alert_id}`);
    return response.data;
}

export async function delete_review_request(request_id) {
    const response = await axios.delete(`${BASE_URL}/review_requests/${request_id}`);
    return response.data;
}
