register_endpoint = '/api/register'

register_payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
        }

register_payload_without_password = {
        "email": "eve.holt@reqres.in"
        }

register_success_response_body = {
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}

register_unsuccess_response_body = {
    "error": "Missing password"
}