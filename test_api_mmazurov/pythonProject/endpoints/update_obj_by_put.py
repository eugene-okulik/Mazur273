import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObj(Endpoint):

    @allure.step('Update object by PUT')
    def make_changes_in_obj(self, obj_id, data):
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=data
        )
        self.json = self.response.json()
        return self.response
