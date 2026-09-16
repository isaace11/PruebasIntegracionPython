import requests


class UserClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_user(self, user_id):
        response = requests.get(
            f"{self.base_url}/users/{user_id}"
        )

        if response.status_code == 404:
            return None

        data = response.json()

        if "first" not in data or "last" not in data:
            return None

        return data
