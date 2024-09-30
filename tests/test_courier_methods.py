import pytest
import allure

from endpoints.courier_methods import CourierMethods as Methods



@allure.feature("Тесты на ручки(методы) раздела Courier: Логин курьера в системе; Создание курьера; Удаление курьера")
class TestCourierMethods:

    @allure.title('Тест на создание курьера')
    def test_create_courier_true(self):
        response = Methods()
        response.post_create_courier()
        response.checking_status_code(201)
        response.checking_response_structure(Methods.SUCCESS_CREATE_COURIER_JSON)

    @allure.title('Тест на создание курьера без обязательного поля login или password')
    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_create_courier_without_field_false(self, param):
        response = Methods()
        response.post_create_courier(without_key=param, key=None, value=None)
        response.checking_status_code(400)

    @allure.title('Тест на создание дубля курьера')
    def test_create_duplicate_courier_false(self):
        response = Methods()
        response.post_create_duplicate_couriers()
        response.checking_status_code(409)
        response.checking_response_structure(Methods.ERROR_CREATE_DUPLICATE_COURIER_JSON)

    @allure.title('Тест на авторизацию курьера и получение id')
    def test_couriers_id_in_system_true(self, create_courier_for_test):
        request_json, response = create_courier_for_test
        response.post_couriers_id_in_system('firstName', request_json, None)
        response.checking_status_code(200)
        response.checking_response_key('id',Methods.SUCCESS_COURIER_ID_IN_SYSTEM)

    @allure.title('Тест на авторизацию курьера без обязательного поля login или password')
    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_get_courier_not_valid_id_in_system_false(self, create_courier_for_test, param):
        request_json, response = create_courier_for_test
        response.post_couriers_id_in_system('firstName', request_json, param)
        response.checking_status_code(404)

    @allure.title('Тест на авторизацию курьера с несуществующими данными')
    def test_get_courier_with_non_existent_id_in_system_false(self, create_courier_for_test):
        request_json, response = create_courier_for_test
        response.post_couriers_id_in_system_for_non_existent_test()
        response.checking_status_code(404)

    @allure.title('Тест на удаление курьера')
    def test_delete_courier_from_system_true(self, id_courier_for_test):
        response, request_json, id_courier = id_courier_for_test
        response.delete_courier_from_base(id_courier)
        response.checking_status_code(200)
        response.checking_response_structure(Methods.SUCCESS_CREATE_COURIER_JSON)
        response.post_couriers_id_in_system('firstName', request_json, None)
        response.checking_status_code(404)

    @allure.title('Тест на удаление курьера с пустым id')
    def test_delete_courier_without_id_false(self, create_courier_for_test):
        request_json, response = create_courier_for_test
        response.delete_courier_from_base("")
        response.checking_status_code(404)

    @allure.title('Тест на удаление курьера с несуществующим id')
    def test_delete_courier_with_non_existent_id_false(self, create_courier_for_test):
        request_json, response = create_courier_for_test
        response.delete_courier_from_base('+100500')
        response.checking_status_code(404)
