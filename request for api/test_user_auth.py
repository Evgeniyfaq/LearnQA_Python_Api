import pytest
import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "There is not auth cookie in the response" #В ответе нет файла cookie для авторизации
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response" #В ответе отсутствует заголовок токена CSRF
        assert "user_id" in response1.json(), "There is no user id in the response" #В ответе нет идентификатора пользователя

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        assert "user_id" in response2.json(), "There is not user id in the second response" #Во втором ответе нет идентификатора пользователя
        user_id_from_check_method = response2.json()["user_id"]
        print(user_id_from_check_method)

        assert user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from check method"
        #Идентификатор пользователя из метода аутентификации не равен идентификатору пользователя из метода проверки


    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "There is not auth cookie in the response"  # В ответе нет файла cookie для авторизации
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"  # В ответе отсутствует заголовок токена CSRF
        assert "user_id" in response1.json(), "There is no user id in the response"  # В ответе нет идентификатора пользователя

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": auth_sid}
            )

        assert "user_id" in response1.json(), "There is not user id in the second response"

        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"User is auth with condition{condition}"




