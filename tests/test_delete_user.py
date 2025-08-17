import allure
import requests
from allure_commons._allure import step
from allure_commons.types import Severity
from conftest import log_teardown, _last_responses

from test_data.general_data import (base_url, headers)
from test_data.delete_user_data import delete_user_endpoint


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода delete /api/users/{user_id}')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Удаление пользователя")
def test_delete_user(log_teardown):
    with step("Отправка запроса на удаление пользователя"):
        response = requests.delete(base_url + delete_user_endpoint, headers=headers)
        _last_responses['current_test'] = response
        with step("Логируем url запроса"):
            allure.attach(body=response.request.url, name="Request URL")
        with step("Логируем статус код"):
            allure.attach(body=str(response.status_code), name="Status code")
    with step("Проверка статуса ответа 204"):
        assert response.status_code == 204
    with step("Проверка отсутствия тела ответа"):
        assert not response.text.strip()



