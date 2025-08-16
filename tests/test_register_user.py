import json
import allure
import requests
from jsonschema import validate
from schemas import register_user_schemas
from allure_commons._allure import step
from allure_commons.types import AttachmentType, Severity

from test_data.general_data import (base_url, headers)
from test_data.register_user_data import (register_endpoint, register_payload, register_payload_without_password,
                                          register_successful_response_body, register_unsuccessful_response_body)


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода post /api/register')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Проверка успешного выполнения запроса /api/register")
def test_register_successful():
    with step("Проверка схемы запроса"):
        request_body = register_payload
        validate(request_body, schema=register_user_schemas.register_successful_request_schema)
    with step("Отправка валидного запроса /api/register"):
        response = requests.post(base_url + register_endpoint, json=register_payload, headers=headers)
        response_body = response.json()
    with step("Проверка статуса ответа 200"):
        assert response.status_code == 200
    with step("Проверка значения response body"):
        assert response_body == register_successful_response_body
    with step("Проверка схемы ответа"):
        validate(response_body, schema=register_user_schemas.register_successful_response_schema)
    with step("Записываем тело ответа"):
        allure.attach(body=json.dumps(response_body, indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода post /api/register')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Проверка неуспешного выполнения запроса /api/register")
def test_register_unsuccessful():
    with step("Проверка схемы запроса"):
        request_body = register_payload_without_password
        validate(request_body, schema=register_user_schemas.register_unsuccessful_request_schema)
    with step("Отправка запроса /api/register без параметра \"password\" в body"):
        response = requests.post(base_url + register_endpoint, json=register_payload_without_password, headers=headers)
        response_body = response.json()
    with step("Проверка статуса ответа 400"):
        assert response.status_code == 400
    with step("Проверка значения response body"):
        assert response_body == register_unsuccessful_response_body
    with step("Проверка схемы ответа"):
        validate(response_body, schema=register_user_schemas.register_unsuccessful_response_schema)
    with step("Записываем тело ответа"):
        allure.attach(body=json.dumps(response_body, indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
