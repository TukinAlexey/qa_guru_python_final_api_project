import json
import allure
import requests
from jsonschema import validate
from schemas import get_user_schemas
from allure_commons._allure import step
from allure_commons.types import AttachmentType, Severity
from conftest import log_teardown, _last_responses

from test_data.general_data import (base_url, headers)
from test_data.get_user_data import  (get_existing_user_endpoint, get_non_existent_user_endpoint,get_existing_user_response_body,
                            get_non_existent_user_response_body)


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода get /api/users/{user_id}')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Получение существующего юзера")
def test_get_existing_user(log_teardown):
    with step("Отправка запроса на получение пользователя"):
        response = requests.get(base_url + get_existing_user_endpoint, headers=headers)
        response_body = response.json()
        _last_responses['current_test'] = response
        with step("Логируем url запроса"):
            allure.attach(body=response.request.url, name="Request URL")
        with step("Логируем тело ответа и статус код"):
            allure.attach(body=json.dumps(response_body, indent=4, ensure_ascii=True), name="Response body",
                          attachment_type=AttachmentType.JSON, extension="json")
            allure.attach(body=str(response.status_code), name="Status code")
    with step("Проверка статуса ответа 200"):
        assert response.status_code == 200
    with step("Проверка значения response body"):
        assert response_body == get_existing_user_response_body
    with step("Проверка схемы ответа"):
        validate(response_body, schema=get_user_schemas.get_existing_user)


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода get /api/users/{user_id}')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Получение несуществующего юзера")
def test_get_non_existent_user(log_teardown):
    with step("Отправка запроса на получение несуществующего пользователя"):
        response = requests.get(base_url + get_non_existent_user_endpoint, headers=headers)
        response_body = response.json()
        _last_responses['current_test'] = response
        with step("Логируем url запроса"):
            allure.attach(body=response.request.url, name="Request URL")
        with step("Логируем тело ответа и статус код"):
            allure.attach(body=json.dumps(response_body, indent=4, ensure_ascii=True), name="Response body",
                          attachment_type=AttachmentType.JSON, extension="json")
            allure.attach(body=str(response.status_code), name="Status code")
    with step("Проверка статуса ответа 404"):
        assert response.status_code == 404
    with step("Проверка значения response body"):
        assert response_body == get_non_existent_user_response_body
    with step("Проверка схемы ответа"):
        validate(response_body, schema=get_user_schemas.get_non_existent_user)
