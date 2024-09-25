from http.client import responses

import configuration
import requests
import data


def get_docs():
     return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# Для получения логов
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":20})

# Для получения инфы из таблицы пользователей
def get_users_table():
     return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# POST для создания нового пользователя
def post_new_user(body):
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# POST для получения набора по продуктам
def post_products_kits(products_ids):
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)
