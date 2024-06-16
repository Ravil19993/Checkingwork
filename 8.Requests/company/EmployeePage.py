import requests
from faker import Faker

fake = Faker("ru_RU")


class Employee:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_list_of_employees(self, my_params):
        resp = requests.get(self.base_url + 'employee',
                            params=my_params)
        return resp.json()

    def get_token(self):
        creds = {
            "username": "raphael",
            "password": "cool-but-crude"
        }
        resp = requests.post(self.base_url + 'auth/login/', json=creds)
        return resp.json()["userToken"]

    def create_employee(self, my_params):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.base_url + 'employee', headers=my_headers,
                             json=my_params)
        return resp.json()

    def get_info_about_employee(self, id):
        resp = requests.get(self.base_url + 'employee/' + str(id))
        return resp.json()

    def change_info(self, id, my_params):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.base_url + 'employee/' + str(id),
                              headers=my_headers, json=my_params)
        return resp.json()
