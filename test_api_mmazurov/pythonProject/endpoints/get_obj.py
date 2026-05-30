import requests
import allure
from endpoints.endpoint import Endpoint


class GetObj(Endpoint):

    @allure.step('Get an obj')
    def get_obj(self, obj_id):
        self.response = requests.get(
            f'{self.url}/{obj_id}'
        )

        try:
            self.json = self.response.json()
        except Exception:
            self.json = None

        return self.response
