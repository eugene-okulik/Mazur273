import pytest
from endpoints.create_obj import CreateObj
from endpoints.update_obj_by_put import UpdateObj
from endpoints.update_obj_by_patch import UpdateObjPatch
from endpoints.delete_obj import DeleteObj
from endpoints.get_obj import GetObj


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
