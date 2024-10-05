import requests

from helpers import create_requests_data, delete_key_and_value_from_json
from scooter_api_links import CourierLinks
from endpoints.base_endpoint import BaseAPI


class CourierMethods(BaseAPI, CourierLinks):
    SUCCESS_CREATE_COURIER_JSON = {"ok": True}
    ERROR_CREATE_DUPLICATE_COURIER_JSON = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."
    }
    SUCCESS_COURIER_ID_IN_SYSTEM = {"id": int}

    def post_create_courier(self, without_key=None, key=None, value=None):
        request_data = create_requests_data(without_key, key, value)
        self.response = requests.post(self.CREATE_COURIER_URL, json=request_data)
        return request_data

    def post_create_duplicate_couriers(self, without_key=None, key=None, value=None):
        request_data = create_requests_data(None, None, None)
        self.response = requests.post(self.CREATE_COURIER_URL, json=request_data)
        self.response = requests.post(self.CREATE_COURIER_URL, json=request_data)

    def post_couriers_id_in_system(self, without_key, value, key):
        request_json = delete_key_and_value_from_json(without_key, value, key)
        self.response = requests.post(self.IS_LOGIN_COURIER_IN_SYSTEM, request_json)
        return self.response.json()

    def delete_courier_from_base(self, id_courier):
        delete_url = CourierLinks.CREATE_COURIER_URL + f'/{id_courier}'
        self.response = requests.delete(delete_url)
        return self.response

    def post_couriers_id_in_system_for_non_existent_test(self):
        request_json = {"login": "BUDDY", "password": "1234"}
        self.response = requests.post(self.IS_LOGIN_COURIER_IN_SYSTEM, request_json)
        return self.response.json()