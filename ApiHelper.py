from requests import request
import json


class ApiHelper:
    def __init__(self):
        self.base_url: str = "http://localhost:5000"
        self.user_url: str = "/users"
        self.headers: dict = {'Content-Type': 'application/json'}

    def create_user(self, payload: dict):
        return request("POST", url=f"{self.base_url}{self.user_url}", headers=self.headers, data=json.dumps(payload))

    def get_user(self, user: str):
        return request("GET", url=f"{self.base_url}{self.user_url}/{user}", headers=self.headers)

    def get_all_users(self):
        return request("GET", url=f"{self.base_url}{self.user_url}", headers=self.headers)

    def edit_user(self, payload: dict, user: str):
        return request("PUT", url=f"{self.base_url}{self.user_url}/{user}", headers=self.headers, data=json.dumps(payload))

    def delete_user(self, user: str):
        return request("DELETE", url=f"{self.base_url}{self.user_url}/{user}", headers=self.headers)
