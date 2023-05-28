import pytest
from utils import get_likes_count
import requests
import allure


@allure.story("Метод likes.add")
@allure.title("Проверка добавления лайка с параметризованными из файла полями type, item_id")
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.add
def test_add_like_multiply_type(params, multi_type, item_id, add_likes_url, get_likes_url):
    params["type"] = multi_type
    params["item_id"] = item_id
    count = get_likes_count(item_id, params)
    response_api = requests.get(add_likes_url, params=params).json()
    count_ex = response_api["response"]["likes"]
    assert count_ex == count + 1
