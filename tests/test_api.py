import requests
from jsonschema import validate
from schemas import register_user_schemas

register_successful_endpoint = '/api/register'
single_user_not_found_endpoint = '/api/users/23'
user_update_endpoint = '/api/users/2'
user_delete_endpoint = '/api/users/2'
user_create_endpoint = '/api/users'


def test_single_user_not_found_endpoint_with_no_response_body():
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.get(url + single_user_not_found_endpoint, headers=headers)
    body = response.json()
    assert body == {}
    assert response.status_code == 404

def test_user_update_check_user_params_after_update_and_response_status_cod():
    name = "morpheus"
    job = "zion resident"
    payload = {
    "name": name,
    "job": job
}
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.put(url + user_update_endpoint, json=payload, headers=headers)
    body = response.json()
    validate(body, schema=schemas.put_user_update)
    assert response.status_code == 200
    assert body["name"] == name
    assert body["job"] == job

def test_user_delete_check_response_status_code():
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.delete(url + user_delete_endpoint,headers=headers)

    assert response.status_code == 204

def test_user_create_check_response_status_and_user_params_after_create():
    name = "morpheus"
    job = "leader"
    payload = {
    "name": name,
    "job": job
}
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.post(url + user_create_endpoint, json=payload, headers=headers)
    body = response.json()
    validate(body, schema=schemas.post_user_create)
    assert response.status_code == 201
    assert body["name"] == name
    assert body["job"] == job