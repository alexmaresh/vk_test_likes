import requests

def get_likes_count(params, get_likes_url, ):
    response = requests.get(get_likes_url, params=params).json()
    return response["response"]["count"]