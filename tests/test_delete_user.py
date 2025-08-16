import allure
import requests
from allure_commons._allure import step
from test_data.general_data import (base_url, headers)
from test_data.delete_user_data import delete_user_endpoint


@allure.tag("API")
@allure.label('owner', 'atukin')
@allure.feature('API tests')
@allure.story('Проверка метода delete /api/users/{user_id}')
@allure.link('https://reqres.in/', name='Testing')
@allure.title("Удаление пользователя")
def test_delete_user():
    with step("Отправка запроса на удаление пользователя"):
        response = requests.delete(base_url + delete_user_endpoint, headers=headers)
    with step("Проверка статуса ответа 204"):
        assert response.status_code == 204
    with step("Проверка отсутствия тела ответа"):
        assert not response.text.strip()



