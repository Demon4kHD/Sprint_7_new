class BaseLink:
    BASEURL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

class CourierLinks:
    CREATE_COURIER_URL = BaseLink.BASEURL + 'courier'
    IS_LOGIN_COURIER_IN_SYSTEM = CREATE_COURIER_URL + '/login'

class OrdersLinks:
    POST_OR_GET_ORDERS = BaseLink.BASEURL + 'orders'
    PUT_FINISH_ORDER = POST_OR_GET_ORDERS + '/finish/'
    PUT_CANCEL_ORDER = POST_OR_GET_ORDERS + '/cancel'
    GET_ORDER_FROM_ID = POST_OR_GET_ORDERS + '/track?t='
    GET_ORDER_FROM_COURIER = POST_OR_GET_ORDERS + '/track?courierId='
    ACCEPT_ORDER = POST_OR_GET_ORDERS + '/accept/'


