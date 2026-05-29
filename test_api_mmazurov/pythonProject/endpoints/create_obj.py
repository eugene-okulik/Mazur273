import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObj(Endpoint):

    @allure.step('Create an obj')
    def new_obj(self, data):
        self.response = requests.post(
            self.url,
            json=data
        )
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None

        return self.response
