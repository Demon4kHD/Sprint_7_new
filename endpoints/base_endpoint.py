
class BaseAPI:
    response = None
    response_json = None

    def checking_response_structure(self, current_body):
        assert current_body == self.response.json()

    def checking_response_key(self, key_value, current_body):
        assert type(self.response.json()[key_value]) == current_body[key_value]

    def checking_status_code(self, value):
        assert self.response.status_code == value
