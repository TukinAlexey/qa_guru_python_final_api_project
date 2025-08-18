# Дипломный проект API на основе сайта https://reqres.in 
## В проекте демонстрируются навыки написания API автотестов с применением разметки и логирования allure, интеграция с jenkins TestOps и Telegram
В проекте проверяется:
- HTTP-методы: GET, POST, DELETE
- Подключено логирование от Allure
- Подключено логирование в консоль
- В тестах присутствуют проверки на:
  - Статус код
  - Значение в response
  - Схему ответа

## Создана инфраструктура проекта
- Создан [билд в jenkins](https://jenkins.autotests.cloud/job/qa_guru_python_final_api_project/)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Jenkins_1.png)
- К прогонам в jenkins добавляется [allure отчет](https://jenkins.autotests.cloud/job/qa_guru_python_final_api_project/12/allure/#suites) в который включено:
  - Шаги прохождение теста
  - Логирование Request URL
  - Логирование Request Body
  - Логирование Status code
  - Логирование Response body
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Allure_1.png)
- Кейсы из прогона добавляются в [TestOps](https://allure.autotests.cloud/project/4885/test-cases?treeId=0)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/TestOps_1.png)
- После прогона в телеграм отправляется отчет о прохождении тестов
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Telegram_1.png)