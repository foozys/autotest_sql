import configuration
import requests
import data
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body)
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDERS_PATH + str(track))
