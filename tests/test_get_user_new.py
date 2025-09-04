import allure
from jsonschema import validate
from schemas import get_user_schemas
from allure_commons._allure import step
from allure_commons.types import Severity
from test_data.general_data import headers
from test_data.get_user_data import (get_existing_user_endpoint, get_non_existent_user_endpoint,
                                     get_existing_user_response_body,
                                     get_non_existent_user_response_body)
from helpers.api_request_helper import api_request


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода get /api/users/{user_id}')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Получение существующего юзера")
def test_get_existing_user():
    with step("Отправка запроса на получение пользователя"):
        response = api_request(method="GET", endpoint=get_existing_user_endpoint, headers=headers, req_body=None)
        response_body = response.json()
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
def test_get_non_existent_user():
    with step("Отправка запроса на получение несуществующего пользователя"):
        response = api_request(method="GET", endpoint=get_non_existent_user_endpoint, headers=headers, req_body=None)
        response_body = response.json()
    with step("Проверка статуса ответа 404"):
        assert response.status_code == 404
    with step("Проверка значения response body"):
        assert response_body == get_non_existent_user_response_body
    with step("Проверка схемы ответа"):
        validate(response_body, schema=get_user_schemas.get_non_existent_user)
