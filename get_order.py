import configuration
import requests
import data

# Выполнить запрос на создание заказа.
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=body)

# Сохранить номер трека заказа.
def get_order_track():
    response = post_new_order(data.order_body)
    return response.json()['track']

# Выполнить запрос на получения заказа по треку заказа.
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + '?t=' + str(track))

# Проверить, что код ответа равен 200.
def test_assert_code_200():
    track_num = get_order_track()
    get_order_response = get_order(track_num)
    # Проверяется, что код ответа равен 200
    assert get_order_response.status_code == 200

# Екатерина Сахнова, 11-я когорта — Финальный проект. Инженер по тестированию плюс
