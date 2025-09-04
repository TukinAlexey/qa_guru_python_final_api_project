import requests
from test_data.general_data import base_url
from helpers.logging_and_attach_helper import response_attaching, response_logging


def api_request(method, endpoint, req_body, **kwargs):
    url = f"{base_url}{endpoint}"
    response = requests.request(method, url, **kwargs)
    response_logging(response)
    response_attaching(response, req_body)
    return response
