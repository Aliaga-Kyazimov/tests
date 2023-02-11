from unittest import TestCase
from Yandex_funcs import get_request, create_directory


class Test(TestCase):
    def test_get(self):
        base_host = "https://cloud-api.yandex.net/"
        token = "" #введите токен
        res = get_request(base_host, token)
        self.assertEqual(res, 200)

    def test_create_directory(self):
        base_host = "https://cloud-api.yandex.net/"
        token = "" #введите токен
        path = "bla-bla"
        res = create_directory(base_host, token, path)
        self.assertEqual(res, 201)
        self.assertEqual(
            res, 409, "Папка с таким названием существует"
        )  # ошибочный тест, но не понятно, как реализовать правильно


if __name__ == "__main__":
    unittest.main()
