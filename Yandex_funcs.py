import requests

# class YaUpLoader:
#     base_host = "https://cloud-api.yandex.net/"
#
#     def __init__(self, token):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             "Content-Type": "application/json",
#             "Authorization": f"OAuth {self.token}",
#         }
#
#     def get_request(self):
#         resp = requests.get(self.base_host, headers=self.get_headers())
#         return resp.status_code
#
#     def create_directory(self, yandex_path):
#         uri = "v1/disk/resources"
#         requests_url = self.base_host + uri
#         params = {"path": yandex_path}
#         resp = requests.put(requests_url, headers=self.get_headers(), params=params)
#         return resp.status_code

# base_host = "https://cloud-api.yandex.net/"


def get_headers(token):
    return {
        "Content-Type": "application/json",
        "Authorization": f"OAuth {token}",
    }


def get_request(base_host, token):
    resp = requests.get(base_host, headers=get_headers(token))
    return resp.status_code


def create_directory(base_host, token, yandex_path):
    uri = "v1/disk/resources"
    requests_url = base_host + uri
    params = {"path": yandex_path}
    resp = requests.put(requests_url, headers=get_headers(token), params=params)
    return resp.status_code
