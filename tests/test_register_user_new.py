import allure
from jsonschema import validate
from schemas import register_user_schemas
from allure_commons._allure import step
from allure_commons.types import Severity
from test_data.general_data import (headers)
from test_data.register_user_data import (register_endpoint, register_payload, register_payload_without_password,
                                          register_successful_response_body, register_unsuccessful_response_body)
from helpers.api_request_helper import api_request


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода post /api/register')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Проверка успешного выполнения запроса /api/register")
def test_register_successful_new():
    with step("Проверка схемы запроса"):
        request_body = register_payload
        validate(request_body, schema=register_user_schemas.register_successful_request_schema)
    with step("Отправка валидного запроса /api/register"):
        response = api_request(method="POST", endpoint=register_endpoint, json=register_payload, headers=headers,
                               req_body=register_payload)
        response_body = response.json()
    with step("Проверка статуса ответа 200"):
        assert response.status_code == 200
    with step("Проверка значения response body"):
        assert response_body == register_successful_response_body
    with step("Проверка схемы ответа"):
        validate(response_body, schema=register_user_schemas.register_successful_response_schema)


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода post /api/register')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Проверка неуспешного выполнения запроса /api/register")
def test_register_unsuccessful_new():
    with step("Проверка схемы запроса"):
        request_body = register_payload_without_password
        validate(request_body, schema=register_user_schemas.register_unsuccessful_request_schema)
    with step("Отправка запроса /api/register без параметра \"password\" в body"):
        response = api_request(method="POST", endpoint=register_endpoint, json=register_payload_without_password,
                               headers=headers,
                               req_body=register_payload_without_password)
        response_body = response.json()
    with step("Проверка статуса ответа 400"):
        assert response.status_code == 400
    with step("Проверка значения response body"):
        assert response_body == register_unsuccessful_response_body
    with step("Проверка схемы ответа"):
        validate(response_body, schema=register_user_schemas.register_unsuccessful_response_schema)
