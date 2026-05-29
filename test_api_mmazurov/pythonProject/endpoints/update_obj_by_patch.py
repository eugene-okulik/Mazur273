import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObjPatch(Endpoint):

    @allure.step('Update object by PATCH')
    def make_changes_in_obj(self, obj_id, data):
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=data
        )
        self.json = self.response.json()
        return self.response
