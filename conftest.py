import json
import os

import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import sessions


def api_requests(service, method, url, **kwargs):
    base_url = {"regres": "https://reqres.in", "catfact": "https://catfact.ninja"}
    new_url = base_url[service] + url
    method = method.upper()
    with allure.step(f"{method} {url}"):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            allure.attach(body=message.encode("utf8"), name="Curl", attachment_type=AttachmentType.TEXT,
                          extension='txt')
            if not response.content:
                allure.attach(body='empty response', name='Empty Response', attachment_type=AttachmentType.TEXT,
                              extension='txt')
            else:
                allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"), name="Response Json",
                              attachment_type=AttachmentType.JSON, extension='json')
    return response


def get_schema(name_of_schema):
    resources_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), os.path.abspath('resources'))
    return os.path.join(resources_path, name_of_schema)
