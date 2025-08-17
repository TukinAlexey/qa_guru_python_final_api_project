from datetime import datetime
import pytest

# Словарь для хранения последних запросов
_last_responses = {}

@pytest.fixture(scope='function', autouse=True)
def log_teardown(request):
    yield  # Выполняем сам тест

    # Проверяем, есть ли сохранённый ответ для текущего теста
    last_response = _last_responses.get('current_test')
    if last_response is not None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nTest name: {request.node.name}")
        print(f"Current date and time: {current_time}")
        print(f"Response status code: {last_response.status_code}")
        print(f"URL: {last_response.request.url}")

    # Если ключ существовал, удаляем его
    if 'current_test' in _last_responses:
        del _last_responses['current_test']