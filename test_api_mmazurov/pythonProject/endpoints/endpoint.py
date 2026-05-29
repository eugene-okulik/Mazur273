import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None

    @allure.step('check the status code')
    def check_response_status_code(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step('chech 400 error returned')
    def check_bad_requests(self):
        assert self.response.status_code == 400
