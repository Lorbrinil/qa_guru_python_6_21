from jsonschema.validators import validate

from conftest import api_requests, get_path_schema, response_schema


def test_status_code_breeds():
    response = api_requests(service='catfact', method='get', url='/breeds', params={"limit": 2})

    assert response.status_code == 200


def test_schema_breeds():
    schema = response_schema(get_path_schema('schema_two_breeds.json'))
    response = api_requests(service='catfact', method='get', url='/breeds', params={"limit": 2})

    validate(instance=response.json(), schema=schema)


def test_max_length_fact():
    response = api_requests(service='catfact', method='get', url='/fact', params={"max_length": 100})

    assert response.json()['length'] <= 100


def test_equality_of_length_fact():
    response = api_requests(service='catfact', method='get', url='/fact', params={"max_length": 100})

    assert len(response.json()['fact']) == response.json()['length']
