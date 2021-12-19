import json

from requests import Response
class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find headers with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]
