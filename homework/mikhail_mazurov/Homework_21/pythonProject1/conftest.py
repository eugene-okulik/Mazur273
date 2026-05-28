import requests
import pytest


@pytest.fixture(scope='session')
def first_and_latest():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def print_before_and_after():
    print('before test')
    yield
    print(' after test')


@pytest.fixture()
def create_obj():
    data = {
        'name': 'Olga',
        'data': {
            'key1': 'value1',
            'key2': 'value2',
        }
    }

    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=data
    )

    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
