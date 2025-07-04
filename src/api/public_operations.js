import axios from "axios";

export async function get_users() {
    const response = await axios.get('http://127.0.0.1:8000/users')
    if (!response.data) {
        alert('Failed to fetch data from the database')
        return 1
    } else {
        return response.data['users']
    }
}

export async function add_user(user) {
    const response = await axios.post('http://127.0.0.1:8000/users', user)
    if (!response.data) {
        alert('Failed to add user to the database')
        return 1
    } else {
        return response.data
    }
}

export async function update_user(user_id, user) {
    const response = await axios.put(`http://127.0.0.1:8000/users/${user_id}`, user);
    return response.data;
}

export async function delete_user(user_id) {
    const response = await axios.delete(`http://127.0.0.1:8000/users/${user_id}`);
    return response.data;
}
// 🏢 Departments
export async function get_departments() {
    const response = await axios.get('http://127.0.0.1:8000/departments');
    return response.data.departments;
}

export async function add_department(department) {
    const response = await axios.post('http://127.0.0.1:8000/departments', department);
    return response.data;
}

export async function update_department(department_id, department) {
    const response = await axios.put(`http://127.0.0.1:8000/departments/${department_id}`, department);
    return response.data;
}

export async function delete_department(department_id) {
    const response = await axios.delete(`http://127.0.0.1:8000/departments/${department_id}`);
    return response.data;
}
