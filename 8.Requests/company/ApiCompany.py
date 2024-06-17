import requests


class ApiCompany:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_token(self, user='raphael', password='cool-but-crude'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.base_url + 'auth/login', json=creds)
        return resp.json()["userToken"]

    def get_list_of_companies(self, my_params):
        resp = requests.get(self.base_url + 'company', params=my_params)
        return resp.json()

    def create_new_company(self, name, description):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.base_url + 'company',
                             headers=my_headers,
                             json={"name": name, "description": description})
        return resp.json()

    def get_info_about_company(self, id):
        resp = requests.get(self.base_url + 'company/' + str(id))
        return resp.json()

    def edit_company(self, id, new_name, new_description):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        my_params = {
            "name": new_name,
            "description": new_description
        }

        resp = requests.patch(self.base_url + 'company/' + str(id),
                              headers=my_headers,
                              json=my_params)
        return resp.json()

    def change_status(self, id, status):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        my_params = {
            "isActive": status
        }

        resp = requests.patch(self.base_url + 'company/status/' + str(id),
                              headers=my_headers, json=my_params)
        return resp.json()

    def delete_company(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.get(self.base_url + 'company/delete/' + str(id),
                            headers=my_headers)
        return resp.json()
