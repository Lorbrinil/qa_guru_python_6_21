from jsonschema.validators import validate

from conftest import api_requests, get_path_schema, response_schema


def test_schema_list_resource():
    schema = response_schema(get_path_schema('schema_list_resource.json'))
    response = api_requests(service='regres', method='get', url='/api/unknown')

    validate(instance=response.json(), schema=schema)


def test_schema_single_user():
    schema = response_schema(get_path_schema('schema_single_user.json'))
    response = api_requests(service='regres', method='get', url='/api/users/2')

    validate(instance=response.json(), schema=schema)
