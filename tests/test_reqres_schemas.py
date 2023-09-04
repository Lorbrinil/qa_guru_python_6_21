import json
from jsonschema.validators import validate

from conftest import api_requests, get_schema


def test_schema_list_resource():
    with open(get_schema('schema_list_resource.json')) as file:
        schema = json.loads(file.read())
    response = api_requests(service='regres', method='get', url='/api/unknown')
        # api_requests(service='regres', method='get', url='/api/unknown')

    validate(instance=response.json(), schema=schema)


def test_schema_single_user():
    with open(get_schema('schema_single_user.json')) as file:
        schema = json.loads(file.read())
    response = api_requests(service='regres', method='get', url='/api/users/2')
        # api_requests(service='regres', method='get', url='/api/users/2')

    validate(instance=response.json(), schema=schema)
