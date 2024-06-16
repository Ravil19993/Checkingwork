import requests
from faker import Faker

fake = Faker("ru_RU")

base_url = 'https://todo-app-sky.herokuapp.com/'


class ToDo:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_list(self):
        resp = requests.get(self.base_url)
        return resp.json()

    def add_deal(self):
        my_params = {
            "title": fake.random_object_name,
            "completed": False
        }
        resp = requests.post(self.base_url, json=my_params)
        return resp.json()

    def rename_deal(self, id):
        my_params = {
            "title": fake.random_object_name
        }
        resp = requests.patch(self.base_url + str(id), json=my_params)
        return resp.json()

    def close_deal(self, id):
        my_params = {
            "completed": True
        }
        resp = requests.patch(self.base_url + str(id), json=my_params)
        return resp.json()

    def recover_deal(self, id):
        my_params = {
            "completed": False
        }
        resp = requests.patch(self.base_url + str(id), json=my_params)
        return resp.json()

    def delete_deal(self, id):
        resp = requests.delete(self.base_url + str(id))
        return resp.json()
