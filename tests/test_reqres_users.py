import datetime
from conftest import api_requests


def test_create_user():
    response = api_requests(service='regres', method='post', url='/api/users',
                            json={"name": "student_name", "job": "student"})

    assert response.status_code == 201
    assert response.json()['name'] == 'student_name'
    assert response.json()['job'] == 'student'


def test_update_user():
    response = api_requests(service='regres', method='put', url='/api/users/2',
                            json={"name": "student_name1", "job": "student1"})

    assert response.status_code == 200
    assert response.json()['name'] == 'student_name1'
    assert response.json()['job'] == 'student1'


def test_update_user_datetime():
    today_utc = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    response = api_requests(service='regres', method='put', url='/api/users/2',
                            json={"name": "student_name2", "job": "student2"})

    assert response.status_code == 200
    assert response.json()['updatedAt'][:-5] == today_utc


def test_delete_user():
    response = api_requests(service='regres', method='delete', url='/api/users/3')

    assert response.status_code == 204


def test_register_new_users():
    response = api_requests(service='regres', method='post', url='/api/register',
                            json={"email": "eve.holt@reqres.in", "password": "pistol123"})

    assert response.status_code == 200
    assert response.json()['id']


def test_error_email_register_new_users():
    response = api_requests(service='regres', method='post', url='/api/register',
                            json={"password": "pistol123"})

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_error_password_register_new_users():
    response = api_requests(service='regres', method='post', url='/api/register',
                            json={"email": "eve.holt@reqres.in"})

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_successful_login():
    response = api_requests(service='regres', method='post', url='/api/login',
                            json={"email": "eve.holt@reqres.in", "password": "pistol123"})

    assert response.status_code == 200
    assert response.json()['token']


def test_unsuccessful_login_with_unknown_user():
    response = api_requests(service='regres', method='post', url='/api/login',
                            json={"email": "unknownuser", "password": "pistol123"})

    assert response.status_code == 400
    assert response.json()['error'] == 'user not found'


def test_check_tokens():
    response_reg = api_requests(service='regres', method='post', url='/api/register',
                                json={"email": "eve.holt@reqres.in", "password": "pistol123"})
    reg_users_token = response_reg.json()['token']
    response_login = api_requests(service='regres', method='post', url='/api/login',
                                  json={"email": "eve.holt@reqres.in", "password": "pistol123"})
    login_users_token = response_login.json()['token']

    assert reg_users_token == login_users_token
