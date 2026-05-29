import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObj(Endpoint):

    @allure.step('Delete an obj')
    def delete_obj(self, obj_id):
        self.response = requests.delete(
            f'{self.url}/{obj_id}'
        )
        return self.response
