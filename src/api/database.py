import pyodbc
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# -*- coding: utf-8 -*-

_DRIVER = 'ODBC Driver 17 for SQL Server'
_SERVER = 'localhost\\SQL2017'
_DATABASE = 'alamana'
CONNECTION_STRING = (
    f"DRIVER={_DRIVER};"
    f"SERVER={_SERVER};"
    f"DATABASE={_DATABASE};"
    "Trusted_Connection=Yes;"
)

def get_connection():
    return pyodbc.connect(CONNECTION_STRING)

api = FastAPI()

# Enable CORS
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@api.get('/')
def root():
    return {'Response': 'Hello, world'}

################################################################

################################################################
@api.get('/users')
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    users = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'users': users}

@api.post('/users')
def add_user(user: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO users 
    (name, email, password, 
    role, department, status)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    cursor.execute(query, (
        user['name'], user['email'], 
        user['password'], user['role'], 
        user['department'], user['status']
        ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'User added successfully'}

@api.get('/users/{user_id}')
def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return {'user': dict(zip(columns, row))}
    return {'user': None}
################################################################

################################################################
@api.get('/departments')
def get_departments():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM departments"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    departments = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'departments': departments}

@api.post('/departments')
def add_department(department: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO departments 
    (name, achieve_ratio)
    VALUES (?, ?);
    """
    cursor.execute(query, (
        department['name'], department['achieve_ratio']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Department added successfully'}

@api.get('/departments/{department_id}')
def get_department_by_id(department_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM departments WHERE id = ?"
    cursor.execute(query, (department_id,))
    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return {'department': dict(zip(columns, row))}
    return {'department': None}
################################################################

################################################################
@api.get('/permissions/{user_id}')
def get_permissions(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM permissions WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    columns = [column[0] for column in cursor.description]
    permissions = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'permissions': permissions}

@api.post('/permissions')
def add_permission(permission: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO permissions 
    (user_id, CAN_CREATE, CAN_READ, CAN_UPDATE, CAN_DELETE)
    VALUES (?, ?, ?, ?, ?);
    """
    cursor.execute(query, (
        permission['user_id'], permission['CAN_CREATE'], 
        permission['CAN_READ'], permission['CAN_UPDATE'], 
        permission['CAN_DELETE']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Permission added successfully'}
################################################################

################################################################
@api.get('/hurryup_alerts')
def get_hurryup_alerts():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM hurryup_alerts"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    alerts = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'hurryup_alerts': alerts}

@api.post('/hurryup_alerts')
def add_hurryup_alert(alert: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO hurryup_alerts 
    (department_id, title, details, status)
    VALUES (?, ?, ?, ?);
    """
    cursor.execute(query, (
        alert['department_id'], alert['title'], 
        alert['details'], alert['status']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Hurry-up alert added successfully'}

@api.get('/hurryup_alerts/{department_id}')
def get_hurryup_alert_by_id(department_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM hurryup_alerts WHERE department_id = ?"
    cursor.execute(query, (department_id,))
    columns = [column[0] for column in cursor.description]
    alerts = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    if alerts:
        return {'hurryup_alerts': alerts}
    return {'hurryup_alerts': []}
################################################################

################################################################
@api.get('/attends')
def get_attends():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM attends"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    attends = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'attends': attends}

@api.get('/attends/{user_id}')
def get_user_attends(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM attends WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    columns = [column[0] for column in cursor.description]
    attends = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'attends': attends}

@api.post('/attends')
def add_attend(attend: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO attends 
    (user_id, attend_date, status)
    VALUES (?, ?, ?);
    """
    cursor.execute(query, (
        attend['user_id'], 
        attend['attend_date'], 
        attend['status']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Attend record added successfully'}
################################################################

################################################################
@api.get('/leaves')
def get_leaves():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM leaves"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    leaves = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'leaves': leaves}

@api.get('/leaves/{user_id}')
def get_user_leaves(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM leaves WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    columns = [column[0] for column in cursor.description]
    leaves = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'leaves': leaves}

@api.post('/leaves')
def add_leave(leave: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO leaves 
    (user_id, title, leave_date, details)
    VALUES (?, ?, ?, ?);
    """
    cursor.execute(query, (
        leave['user_id'], leave['title'], 
        leave['leave_date'], leave['details']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Leave request added successfully'}
################################################################

################################################################
@api.get('/missions/{user_id}')
def get_user_missions(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM missions WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    columns = [column[0] for column in cursor.description]
    missions = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'missions': missions}

@api.post('/missions')
def add_mission(mission: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO missions 
    (user_id, title, text, deadline_date, status)
    VALUES (?, ?, ?, ?, ?);
    """
    cursor.execute(query, (
        mission['user_id'], mission['title'], 
        mission['text'], mission['deadline_date'], 
        mission['status']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Mission added successfully'}
################################################################

################################################################
@api.get('/notifications/{user_id}')
def get_user_notifications(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM notifications WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    columns = [column[0] for column in cursor.description]
    notifications = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'notifications': notifications}

@api.post('/notifications')
def add_notification(notification: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO notifications 
    (user_id, text, status)
    VALUES (?, ?, ?);
    """
    cursor.execute(query, (
        notification['user_id'], 
        notification['text'], 
        notification['status']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Notification added successfully'}
################################################################

################################################################
@api.get('/review-requests/{department_id}')
def get_review_requests(department_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM review_requests WHERE department_id = ?"
    cursor.execute(query, (department_id,))
    columns = [column[0] for column in cursor.description]
    review_requests = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'review_requests': review_requests}

@api.post('/review-requests')
def add_review_request(review_request: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO review_requests 
    (department_id, user_id, text, status)
    VALUES (?, ?, ?, ?);
    """
    cursor.execute(query, (
        review_request['department_id'],
        review_request['user_id'],
        review_request['text'],
        review_request['status']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Review request added successfully'}
################################################################

################################################################
@api.get('/reports')
def get_reports():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM reports"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    reports = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'reports': reports}

@api.get('/reports/{department_id}')
def get_department_reports(department_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM reports WHERE department_id = ?"
    cursor.execute(query, (department_id,))
    columns = [column[0] for column in cursor.description]
    reports = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'reports': reports}

@api.post('/reports')
def add_report(report: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO reports 
    (department_id, type, report_date, status)
    VALUES (?, ?, ?, ?);
    """
    cursor.execute(query, (
        report['department_id'],
        report['type'],
        report['report_date'],
        report['status']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Report added successfully'}
################################################################

################################################################
@api.get('/major-requests/{department_id}')
def get_major_requests(department_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM major_requests WHERE department_id = ?"
    cursor.execute(query, (department_id,))
    columns = [column[0] for column in cursor.description]
    major_requests = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {'major_requests': major_requests}

@api.post('/major-requests')
def add_major_request(major_request: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = \
    """
    INSERT INTO major_requests 
    (department_id, request_type, description, status)
    VALUES (?, ?, ?, ?);
    """
    cursor.execute(query, (
        major_request['department_id'],
        major_request['request_type'],
        major_request['description'],
        major_request['status']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Major request added successfully'}
################################################################

################################################################


################################################################

################################################################
@api.delete('/users/{user_id}')
def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'User deleted successfully'}
################################################################

################################################################
@api.delete('/departments/{department_id}')
def delete_department(department_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM departments WHERE id = ?"
    cursor.execute(query, (department_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Department deleted successfully'}
################################################################

################################################################
@api.delete('/notifications/{notification_id}')
def delete_notification(notification_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM notifications WHERE id = ?"
    cursor.execute(query, (notification_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Notification deleted successfully'}
################################################################

################################################################
@api.delete('/missions/{mission_id}')
def delete_mission(mission_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM missions WHERE id = ?"
    cursor.execute(query, (mission_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Mission deleted successfully'}
################################################################

################################################################
@api.delete('/major-requests/{request_id}')
def delete_major_request(request_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM major_requests WHERE id = ?"
    cursor.execute(query, (request_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Major request deleted successfully'}
################################################################

################################################################
@api.delete('/hurryup-alerts/{alert_id}')
def delete_hurryup_alert(alert_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM hurryup_alerts WHERE id = ?"
    cursor.execute(query, (alert_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Hurry-up alert deleted successfully'}
################################################################

################################################################
@api.delete('/review-requests/{request_id}')
def delete_review_request(request_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM review_requests WHERE id = ?"
    cursor.execute(query, (request_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Review request deleted successfully'}

################################################################

################################################################

@api.delete('/reports/{report_id}')
def delete_report(report_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM reports WHERE id = ?"
    cursor.execute(query, (report_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Report deleted successfully'}
################################################################

################################################################


################################################################

################################################################
@api.put('/users/{user_id}')
def update_user(user_id: int, user: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET name = ?, email = ?, password = ?, role = ? WHERE id = ?"
    cursor.execute(query, (user['name'], user['email'], user['password'], user['role'], user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'User updated successfully'}
################################################################

################################################################
@api.put('/departments/{department_id}')
def update_department(department_id: int, department: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE departments SET name = ?, achieve_ratio = ? WHERE id = ?"
    cursor.execute(query, (department['name'], department['achieve_ratio'], department_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Department updated successfully'}
################################################################

################################################################
api.put('/missions/{mission_id}')
def update_mission(mission_id: int, mission: dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE missions SET title = ?, description = ?, status = ? WHERE id = ?"
    cursor.execute(query, (mission['title'], mission['description'], mission['status'], mission_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Mission updated successfully'}