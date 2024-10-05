import requests

from endpoints.base_endpoint import BaseAPI
from scooter_api_links import OrdersLinks


class OrdersMethods(BaseAPI, OrdersLinks):
    SUCCESS_CREATE = {
        "track": int
    }
    ORDERS_JSON = {"firstName": "Naruto", "lastName": "Uchiha", "address": "Konoha, 142 apt.", "metroStation": 4,
                   "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2024-10-02",
                   "comment": "Saske, come back to Konoha", "color": []}
    SUCCESS_ACCEPT_ORDER = {
                            "ok": True
                            }

    def post_create_order(self, value):
        orders_json_for_create = self.ORDERS_JSON
        orders_json_for_create['color'] = value
        self.response = requests.post(OrdersLinks.POST_OR_GET_ORDERS, json=orders_json_for_create)
        return self.response

    def get_len_response_json(self, response_json):
        len_response_json = len(response_json["orders"])
        return len_response_json

    def get_orders_list(self):
        self.response = requests.get(OrdersLinks.POST_OR_GET_ORDERS)
        self.response_json = self.response.json()
        return  self.response, self.response_json

    def checking_length_orders_list(self, limit):
        len_response_json = self.get_len_response_json(self.response_json)
        assert len_response_json == limit

    def get_response_json(self):
        self.response_json = self.response.json()
        return self.response_json

    def put_cansel_order(self, order_id_json):
        self.response = requests.put(OrdersLinks.PUT_CANCEL_ORDER, json=order_id_json)
        return self.response

    def put_accept_order(self, order_id, id_courier):
        if order_id == None:
            checked_url = OrdersLinks.ACCEPT_ORDER + f"?courierId={id_courier}"
        elif id_courier == None:
            checked_url = OrdersLinks.ACCEPT_ORDER + f"{order_id}?courierId="
        else:
            checked_url = OrdersLinks.ACCEPT_ORDER + f"{order_id}?courierId={id_courier}"
        self.response = requests.put(checked_url)
        return self.response

    def get_order_by_id(self, orders_id):
        if orders_id == None:
            checked_url = OrdersLinks.GET_ORDER_FROM_ID
        else:
            checked_url = OrdersLinks.GET_ORDER_FROM_ID + f"{orders_id}"
        self.response = requests.get(checked_url)
        self.response_json_2 = self.response.json()
        return self.response, self.response_json_2


