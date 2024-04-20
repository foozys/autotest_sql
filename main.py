import data
import test


def test_created_order_exists_in_database_1():

    response = test.post_new_order(data.order_body)
    track = response.json()["track"]

    user_response = test.get_order(track)
    assert user_response.status_code == 200

#Фирсов Владислав, 15 когорта - Финальный проект. Инженер по тестированию плюс