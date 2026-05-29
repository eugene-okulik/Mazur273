import pytest
from data.data import (
    TEST_DATA,
    NEGATIVE_DATA,
    PUT_DATA,
    PATCH_DATA
)


@pytest.mark.parametrize('data', TEST_DATA)
def test_get_obj(create_obj, get_obj_endpoint):
    get_obj_endpoint.get_obj(create_obj)
    get_obj_endpoint.check_response_status_code()


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_new_obj_with_neg_data(create_obj_endpoint, data):
    create_obj_endpoint.new_obj(data)
    create_obj_endpoint.check_bad_requests()


@pytest.mark.parametrize('data', PUT_DATA)
def test_put_obj(create_obj, update_obj_endpoint, data):
    update_obj_endpoint.make_changes_in_obj(create_obj, data)
    update_obj_endpoint.check_response_status_code()


@pytest.mark.parametrize('data', PATCH_DATA)
def test_patch_obj(create_obj, update_obj_patch_endpoint, data):
    update_obj_patch_endpoint.make_changes_in_obj(create_obj, data)
    update_obj_patch_endpoint.check_response_status_code()


def test_delete_obj(created_obj_without_cleanup, delete_obj_endpoint):
    delete_obj_endpoint.delete_obj(created_obj_without_cleanup)
    delete_obj_endpoint.check_response_status_code()


def test_get_obj(create_obj_endpoint, get_obj_endpoint):
    create_obj_endpoint.new_obj({
        'name': 'Olga',
        'data': {'key3': 'value3'}
    })
    obj_id = create_obj_endpoint.json['id']
    get_obj_endpoint.get_obj(obj_id)
    get_obj_endpoint.check_response_status_code()
