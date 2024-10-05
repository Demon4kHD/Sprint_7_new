import random

from urllib3 import request


def create_value_for_current_key(num_keys, length_key):
    symbols_for_current_keys = 'abcdefghijklmnopqrstuvwxyz'
    numbers_for_current_keys = '0123456789'
    current_key = ''

    for i in range(length_key):
        if num_keys == True:
            current_key += random.choice(numbers_for_current_keys)
        else:
            current_key += random.choice(symbols_for_current_keys)
    return current_key

def create_requests_data(without_key, key, value):
    keys = ["login", "password", "firstName"]
    request_data = {}
    for i in keys:
        if i == key:
            if i != "password":
                request_data[i] = create_value_for_current_key(False, value)
            else:
                request_data[i] = create_value_for_current_key(True, value)
        elif i == without_key:
            continue
        else:
            if i != "password":
                request_data[i] = create_value_for_current_key(False, 4)
            else:
                request_data[i] = create_value_for_current_key(True,10)
    return request_data

def delete_key_and_value_from_json(without_key, request_json, key):
    new_request_json = {}
    for i in request_json:
        if i == without_key:
            continue
        elif i == key:
            if i == "password":
                new_request_json[i] = create_value_for_current_key(True, 4)
            else:
                new_request_json[i] = create_value_for_current_key(False, 10)
        else:
            new_request_json[i] = request_json[i]
    return new_request_json
