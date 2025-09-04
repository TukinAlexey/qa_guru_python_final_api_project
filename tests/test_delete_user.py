import allure
from allure_commons._allure import step
from allure_commons.types import Severity
from test_data.general_data import headers
from test_data.delete_user_data import delete_user_endpoint
from helpers.api_request_helper import api_request


@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода delete /api/users/{user_id}')
@allure.link('https://reqres.in/', name='REQRES')
@allure.title("Удаление пользователя")
def test_delete_user():
    with step("Отправка запроса на удаление пользователя"):
        response = api_request(method="DELETE", endpoint=delete_user_endpoint, headers=headers, req_body=None)
    with step("Проверка статуса ответа 204"):
        assert response.status_code == 204
    with step("Проверка отсутствия тела ответа"):
        assert not response.text.strip()
