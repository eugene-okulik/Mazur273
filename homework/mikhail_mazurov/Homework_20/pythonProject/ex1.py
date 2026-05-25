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


def test_get_all_obj(print_before_and_after, first_and_latest):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(f'статус-код: {response.status_code}')
    assert response.status_code == 200, 'Что-то пошло не так'
    print(f'тип данных: {type(response.json())}')


def test_one_obj(print_before_and_after):
    response = requests.get('http://objapi.course.qa-practice.com/object/1')
    print(f'статус-код получения объекта: {response.status_code}')


@pytest.mark.parametrize('names', ['Mikhail', 'Eugene', 'Polina'])
def test_new_obj(names, print_before_and_after):
    data = {'name': names,
            'data': {
                'key1': 'value1',
                'key2': 'value2',
            }}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=data
    )
    assert response.status_code == 200, 'Status code is incorrect'
    obj_id = response.json()['id']
    print(f'новый объект создан, id {obj_id}')

@pytest.mark.critical
def test_put_obj(print_before_and_after, create_obj):
    obj_id = create_obj
    name = "Mikhail_UPD"
    data = {'name': name,
            'data': {
                'key1_upd': 'value1_upd',
                'key2_upd': 'value2_upd',
            }}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{obj_id}',
        json=data
    )
    assert response.status_code == 200, 'Объект не изменен'
    print(response.status_code)

@pytest.mark.medium
def test_patch_obj(create_obj):
    obj_id = create_obj
    name = "Mikhail_PATCH"
    data = {'name': name,
            'data': {
                'key1_upd': 'value1_upd',
                'key2_upd': 'value2_upd',
            }}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{obj_id}',
        json=data
    )
    assert response.status_code == 200, 'Объект не изменен'
    print(response.status_code)


def test_delete_obj(create_obj):
    # тут получается удаляем объект, а потом фикстура его пытается удалить
    # в реальных условиях вернет 404 скорее всего, да и тест избыточен так как
    # удаление тестируется в фикстуре но без фикстуры я не уверен откуда
    # брать тогда obj_id - test_new_obj теперь вернет 3 obj_id и его не вставить в аргументы
    obj_id = create_obj
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    assert response.status_code == 200
    print(f'объект с id {obj_id} удален')
