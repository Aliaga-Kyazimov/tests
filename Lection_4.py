# Задание №1
geo_logs = [
    {"visit1": ["Москва", "Россия"]},
    {"visit2": ["Дели", "Индия"]},
    {"visit3": ["Владимир", "Россия"]},
    {"visit4": ["Лиссабон", "Португалия"]},
    {"visit5": ["Париж", "Франция"]},
    {"visit6": ["Лиссабон", "Португалия"]},
    {"visit7": ["Тула", "Россия"]},
    {"visit8": ["Тула", "Россия"]},
    {"visit9": ["Курск", "Россия"]},
    {"visit10": ["Архангельск", "Россия"]},
    {"visit11": ["Владимир", "Россия"]},
    {"visit12": ["Пекин", "Китай"]},
]


def find_visit(geo_logs_list):
    geo_logs_new = []
    for i in geo_logs_list:
        for key, value in i.items():
            if "Россия" in value:
                geo_logs_new.append(i)
    return geo_logs_new


# Задание №2
ids = {
    "user1": [213, 213, 213, 15, 213],
    "user2": [54, 54, 119, 119, 119],
    "user3": [213, 98, 98, 35],
}


def list_of_values(list_):
    list_new = []
    for values in list_.values():
        for value in values:
            if value not in list_new:
                list_new.append(value)
    return list_new


#
# #Задание №3
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт',
#     ]
#
# list_new = []
# dict_new ={}
#
# for object in queries:
#     object = object.split()
#     list_new.append(len(object))
#     total_requests = len(list_new)
#     for key in list_new:
#         dict_new.setdefault(key)
#         for key, value in dict_new.items():
#             total = 0
#             for i in list_new:
#                 if i == key:
#                     total += 1
#                 else:
#                     pass
#             dict_new[key] = total
#
# for key, value in dict_new.items():
#     print(f"Поисковых запросов из {key} слов {round((value * 100)/total_requests)}%")
#
# Задание №4
stats = {
    "facebook": 55,
    "yandex": 120,
    "vk": 115,
    "google": 99,
    "email": 42,
    "ok": 98,
    "apple": 119,
}


def max_value(dict_):
    result_max = 0
    for value in dict_.values():
        if value > result_max:
            result_max = value
    return list(dict_.keys())[list(dict_.values()).index(result_max)]


# #Задание №5
# list_1 = ['2018-01-01', 'yandex', 'cpc', 100]
# dict_res = {list_1[-2] : list_1[-1]}
#
# list_1 = list_1[:(len(list_1) - 2)]
# i = -1
#
# for elements in list_1:
#     dict_res = {list_1[i] : dict_res}
#     i -= 1
#
# print(dict_res)
