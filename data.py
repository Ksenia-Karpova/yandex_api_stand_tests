# заголовки для HTTP-запроса, указывают, что тело запроса будет в JSON
headers = {
    "Content-Type": "application/json"
}

# данные для создания новой записи пользователя в системе
user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

# данные для получения набора по продуктам
product_ids = {
    "ids": [1, 2, 3]
}