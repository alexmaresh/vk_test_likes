import requests


# Тестовый метод, проверить доступ в апишку
def test_likes_count(params, get_likes_url, headers):
    response = requests.get(get_likes_url, params=params, headers=headers).json()
    assert response["response"]["count"] == 25
