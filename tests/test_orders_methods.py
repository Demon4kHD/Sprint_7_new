import pytest
import allure

from endpoints.orders_methods import OrdersMethods as Methods


@allure.feature("Тесты на ручки(методы) раздела Orders: Создание заказа; Принятие заказа; Получение списка заказов; "
                "Получить заказ по его номеру")
class TestOrdersMethods:

    @allure.title('Тест на создание заказа')
    @pytest.mark.parametrize('value', [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_order_true(self, value):
        response = Methods()
        response.post_create_order(value)
        response.checking_status_code(201)
        response.checking_response_key('track', Methods.SUCCESS_CREATE)

    @allure.description("Долгое время ожидания ответа при проведении теста")
    @allure.title('Тест на список заказов')
    def test_get_orders_list(self):
        response = Methods()
        response.get_orders_list()
        response.checking_status_code(200)
        response.checking_length_orders_list(30)

    @allure.title('Тест на получение заказа по его номеру')
    def test_get_order_by_order_id(self, create_order_id_for_test):
        orders_response, orders_id, order_id_json = create_order_id_for_test
        orders_response.get_order_by_id(orders_id)
        orders_response.checking_status_code(200)

    @allure.title('Тест на получение заказа без номера')
    def test_get_order_by_none_order_id(self, create_order_id_for_test):
        orders_response, orders_id, order_id_json = create_order_id_for_test
        orders_response.get_order_by_id(None)
        orders_response.checking_status_code(400)

    @allure.title('Тест на получение заказа по несуществующему номеру')
    def test_get_order_by_non_existent_order_id(self, create_order_id_for_test):
        orders_response, orders_id, order_id_json = create_order_id_for_test
        orders_response.get_order_by_id(999100500)
        orders_response.checking_status_code(404)

    @allure.description("Некорректное поведение при проведении теста")
    @allure.title('Тест на принятие заказа по номеру заказа и по номеру курьера')
    def test_accept_order_by_courier(self, create_id_courier_and_order_id_for_test):
        response, courier_request_json, id_courier, orders_response, orders_id, order_id_json = create_id_courier_and_order_id_for_test
        orders_response.put_accept_order(orders_id, id_courier)
        orders_response.checking_response_structure(Methods.SUCCESS_ACCEPT_ORDER)

    @allure.title('Тест на принятие заказа по номеру заказа и по несуществующему номеру курьера')
    def test_accept_order_by_courier_by_non_existent_courier_id(self, create_id_courier_and_order_id_for_test):
        response, courier_request_json, id_courier, orders_response, orders_id, order_id_json = create_id_courier_and_order_id_for_test
        orders_response.put_accept_order(orders_id, "999100500")
        orders_response.checking_status_code(404)

    @allure.title('Тест на принятие заказа по номеру заказа и без номера курьера')
    def test_accept_order_by_courier_by_none_id_courier(self, create_id_courier_and_order_id_for_test):
        response, courier_request_json, id_courier, orders_response, orders_id, order_id_json = create_id_courier_and_order_id_for_test
        orders_response.put_accept_order(orders_id, None)
        orders_response.checking_status_code(400)

    @allure.title('Тест на принятие заказа по несуществующему номеру заказа и по номеру курьера')
    def test_accept_order_by_courier_by_non_existent_orders_id(self, create_id_courier_and_order_id_for_test):
        response, courier_request_json, id_courier, orders_response, orders_id, order_id_json = create_id_courier_and_order_id_for_test
        orders_response.put_accept_order("999100500", id_courier)
        orders_response.checking_status_code(404)

    @allure.description("Некорректное поведение при проведении теста")
    @allure.title('Тест на принятие заказа без номера заказа и по номеру курьера')
    def test_accept_order_by_courier_by_none_orders_id(self, create_id_courier_and_order_id_for_test):
        response, courier_request_json, id_courier, orders_response, orders_id, order_id_json = create_id_courier_and_order_id_for_test
        orders_response.put_accept_order(None, id_courier)
        orders_response.checking_status_code(400)
