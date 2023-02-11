from unittest import TestCase
from Lection_4 import find_visit, list_of_values, max_value


class Test(TestCase):
    def test_visits(self):
        geo_logs_test = [
            {"visit1": ["Москва", "Россия"]},
            {"visit2": ["Дели", "Индия"]},
            {"visit3": ["Владимир", "Россия"]},
        ]
        res = find_visit(geo_logs_test)
        self.assertEqual(
            res, [{"visit1": ["Москва", "Россия"]}, {"visit3": ["Владимир", "Россия"]}]
        )

    def test_ids(self):
        ids = {
            "user1": [213, 213, 213, 15, 213],
            "user2": [54, 54, 119, 119, 119],
            "user3": [213, 98, 98, 35],
        }
        res = list_of_values(ids)
        self.assertEqual(res, [213, 15, 54, 119, 98, 35])

    def test_max_value(self):
        stats = {
            "facebook": 55,
            "yandex": 120,
            "vk": 115,
            "google": 99,
            "email": 42,
            "ok": 98,
            "apple": 119,
        }
        res = max_value(stats)
        self.assertEqual(res, "yandex")


if __name__ == "__main__":
    unittest.main()
