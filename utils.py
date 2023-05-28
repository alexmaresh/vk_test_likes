import requests
from config import API_ADD_LIKES, API_IS_LIKED, API_DEL_LIKES, API_GET_LIKES

def get_likes_count(post_id, params):
    params["item_id"] = post_id
    response = requests.get(API_GET_LIKES, params=params).json()
    return response["response"]["count"]


def get_is_liked(post_id, params):
    params["item_id"] = post_id
    response = requests.get(API_IS_LIKED, params=params).json()
    return response["response"]["liked"]


def delete_like(post_id, params):
    params["item_id"] = post_id
    try:
        response = requests.get(API_DEL_LIKES, params=params).json()
        return response["response"]["likes"]
    except Exception as e:
        raise Exception(f"Ошибка при удалении лайка у поста: {e}")


def add_like(post_id, params):
    params["item_id"] = post_id
    try:
        response = requests.get(API_ADD_LIKES, params=params).json()
        return response["response"]["likes"]
    except Exception as e:
        raise Exception(f"Ошибка при постановке лайка посту: {e}")
