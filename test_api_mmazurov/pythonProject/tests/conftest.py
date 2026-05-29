import pytest
from endpoints.create_obj import CreateObj
from endpoints.update_obj_by_put import UpdateObj
from endpoints.update_obj_by_patch import UpdateObjPatch
from endpoints.delete_obj import DeleteObj
from endpoints.get_obj import GetObj



@pytest.fixture
def create_obj():
    create_endpoint = CreateObj()
    delete_endpoint = DeleteObj()

    payload = {
        'name': 'Mikhail',
        'data': {'key1': 'value1'}
    }

    response = create_endpoint.new_obj(payload)
    obj_id = create_endpoint.json['id']

    yield obj_id

    delete_endpoint.delete_obj(obj_id)

@pytest.fixture
def created_obj_without_cleanup():
    create_endpoint = CreateObj()

    payload = {
        'name': 'Mikhail',
        'data': {'key1': 'value1'}
    }

    create_endpoint.new_obj(payload)
    return create_endpoint.json['id']


@pytest.fixture
def get_obj_endpoint():
    return GetObj()


@pytest.fixture
def delete_obj_endpoint():
    return DeleteObj()


@pytest.fixture()
def create_obj_endpoint():
    return CreateObj()


@pytest.fixture
def update_obj_endpoint():
    return UpdateObj()


@pytest.fixture
def update_obj_patch_endpoint():
    return UpdateObjPatch()
