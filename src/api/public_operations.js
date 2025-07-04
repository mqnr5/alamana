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

export async function add_dapartment(department) {
    const response = await axios.post('http://127.0.0.1:8000/departments', department)
    if (!response.data) {
        alert('Failed to add department to the database')
        return 1
    } else {
        return response.data
    }
}

