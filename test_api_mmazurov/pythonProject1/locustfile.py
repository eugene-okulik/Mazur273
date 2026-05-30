from locust import task, HttpUser
from data.data import (
    TEST_DATA,
    PUT_DATA,
    PATCH_DATA
)


class ObjForLocust(HttpUser):
    obj_id = None

    def on_start(self):
        response = self.client.post(
            '/object',
            json=TEST_DATA
        )
        self.obj_id = response.json()['id']

    def on_stop(self):
        self.client.delete(
            f'/object/{self.obj_id}'
        )

    @task
    def get_all_obj(self):
        self.client.get(
            '/object'
        )

    @task
    def get_one_obj(self):
        self.client.get(
            f'/object/{self.obj_id}'
        )

    @task
    def put_obj(self):
        self.client.put(
            f'/object/{self.obj_id}',
            json=PUT_DATA
        )

    @task
    def patch_obj(self):
        self.client.patch(
            f'/object/{self.obj_id}',
            json=PATCH_DATA
        )
