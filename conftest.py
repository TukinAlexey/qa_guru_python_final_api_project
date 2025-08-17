import pytest
import requests

# Словарь для хранения последних запросов
_last_responses = {}

@pytest.fixture(scope='function', autouse=True)
def log_teardown():
    yield  # Выполняем сам тест

    # Проверяем, есть ли сохранённый ответ для текущего теста
    last_response = _last_responses.get('current_test')
    if last_response is not None:
        print(f"\nURL: {last_response.request.url}")
        print(f"Код ответа: {last_response.status_code}")

    # Если ключ существовал, удаляем его
    if 'current_test' in _last_responses:
        del _last_responses['current_test']