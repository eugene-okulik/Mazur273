import pytest


TEST_DATA = [
    {'name': 'Mikhail', 'data': {'key1': 'value1'}},
    {'name': 'Olga', 'data': {'key2': 'value2'}}
]

NEGATIVE_DATA = [
    {'name': ['Mikhail'], 'data': {'key1': 'value1'}},
    {'name': {'Olga': ''}, 'data': {'key2': 'value2'}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_new_obj(create_obj_endpoint, data):
    create_obj_endpoint.new_obj(data)
    create_obj_endpoint.check_response_status_code()
    obj_id = create_obj_endpoint.json['id']
    print(f'новый объект создан, id {obj_id}')


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_new_obj_with_neg_data(create_obj_endpoint, data):
    create_obj_endpoint.new_obj(data)
    create_obj_endpoint.check_bad_requests()


PUT_DATA = [
    {'name': 'Mikhail_UPD_by_PUT', 'data': {'key1': 'value1'}}
]


@pytest.mark.parametrize('data', PUT_DATA)
def test_put_obj(create_obj_endpoint, update_obj_endpoint, data):
    create_obj_endpoint.new_obj({
        'name': 'Mikhail',
        'data': {'key1': 'value1'}
    })
    obj_id = create_obj_endpoint.json['id']
    update_obj_endpoint.make_changes_in_obj(obj_id, data)
    update_obj_endpoint.check_response_status_code()


PATCH_DATA = [{'name': 'Mikhail_UPD_by_PATCH'}]


@pytest.mark.parametrize('data', PATCH_DATA)
def test_patch_obj(create_obj_endpoint, update_obj_patch_endpoint, data):
    create_obj_endpoint.new_obj({
        'name': 'Mikhail',
        'data': {'key1': 'value1'}
    })
    obj_id = create_obj_endpoint.json['id']
    update_obj_patch_endpoint.make_changes_in_obj(obj_id, data)
    update_obj_patch_endpoint.check_response_status_code()


def test_delete_obj(create_obj_endpoint, delete_obj_endpoint):
    create_obj_endpoint.new_obj({
        'name': 'Mikhail',
        'data': {'key1': 'value1'}
    })
    obj_id = create_obj_endpoint.json['id']
    delete_obj_endpoint.delete_obj(obj_id)
    delete_obj_endpoint.check_response_status_code()


def test_get_obj(create_obj_endpoint, get_obj_endpoint):
    create_obj_endpoint.new_obj({
        'name': 'Olga',
        'data': {'key3': 'value3'}
    })
    obj_id = create_obj_endpoint.json['id']
    get_obj_endpoint.get_obj(obj_id)
    get_obj_endpoint.check_response_status_code()
