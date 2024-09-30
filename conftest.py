import pytest

from endpoints.courier_methods import CourierMethods as Courier
from endpoints.orders_methods import  OrdersMethods as Order


@pytest.fixture
def create_courier_for_test():
    response = Courier()
    request_json = response.post_create_courier()
    return request_json, response


@pytest.fixture
def id_courier_for_test(create_courier_for_test):
    request_json, response = create_courier_for_test
    request_id_courier = response.post_couriers_id_in_system("firstName", request_json, None)
    id_courier = request_id_courier["id"]
    yield response, request_json, id_courier
    response.delete_courier_from_base(id_courier)

@pytest.fixture
def create_order_id_for_test():
    orders_response = Order()
    orders_response.post_create_order(["BLACK"])
    order_id_json = orders_response.get_response_json()
    orders_id = order_id_json["track"]
    yield orders_response, orders_id, order_id_json
    orders_response.put_cansel_order(order_id_json)

@pytest.fixture
def create_id_courier_and_order_id_for_test(id_courier_for_test, create_order_id_for_test):
    response, courier_request_json, id_courier = id_courier_for_test
    orders_response, orders_id, order_id_json = create_order_id_for_test
    return  response, courier_request_json, id_courier, orders_response, orders_id, order_id_json
