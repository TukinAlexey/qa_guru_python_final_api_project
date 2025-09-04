import logging
import json
import allure
from requests import Response
from allure_commons.types import AttachmentType


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + str(response.request.body))  # логирование тела запроса если оно есть
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    if not response.text.strip():
        logging.info("Response is empty")
    else:
        logging.info("Response: " + response.text)


def response_attaching(response: Response, req_body):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=str(response.status_code),
        name="Status code",
        attachment_type=AttachmentType.TEXT,
    )
    if response.request.body:
        allure.attach(
            body=json.dumps(req_body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    try:
        # Пробуем извлечь JSON из ответа
        resp_json = response.json()
        allure.attach(
            body=json.dumps(resp_json, indent=4, ensure_ascii=False),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    except ValueError as e:
        # Обрабатываем случай, когда ответ не является JSON
        print(f"При выполнении запроса получен пустой ответ: {e}")
        allure.attach(
            body=str(response.text),
            name="Response is empty",
            attachment_type=AttachmentType.TEXT,
        )
