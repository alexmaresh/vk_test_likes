import pytest
import requests
import allure

from utils import get_likes_count, get_is_liked
from config import POSTS


@allure.story("Метод likes.add")
@allure.title("Проверка корректности ответа метода add на валидные параметры")
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.add
@pytest.mark.parametrize("post_id", POSTS)
def test_add_params(post_id, params, add_likes_url):
    params["item_id"] = post_id
    response_api = requests.get(add_likes_url, params=params).json()
    assert response_api["response"]["likes"], "В ответе нет поля likes"
    assert int(response_api["response"]["likes"]), "Формат поля likes != int"


@allure.story("Метод likes.delete")
@allure.title("Проверка корректности ответа метода delete на валидные параметры")
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.delete
@pytest.mark.parametrize("post_id", POSTS)
def test_del_params(post_id, params, del_likes_url):
    params["item_id"] = post_id
    response_api = requests.get(del_likes_url, params=params).json()
    assert response_api["response"]["likes"], "В ответе нет поля likes"
    assert int(response_api["response"]["likes"]), "Формат поля likes != int"


@allure.story("Метод likes.add")
@allure.title("Проверка добавления лайка посту")
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.add
def test_add_like(not_liked_post, params, add_likes_url, get_likes_url, get_is_liked_url):
    post = not_liked_post["post_id"]
    params["item_id"] = post
    count = get_likes_count(post, params)
    response_api = requests.get(add_likes_url, params=params).json()
    count_ex = response_api["response"]["likes"]
    assert get_is_liked(post, params), "Пост не добавлен в раздел 'Мне нравится' пользователю"
    assert count_ex == count + 1


@allure.story("Метод likes.delete")
@allure.title("Проверка удаления лайка у поста")
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.delete
def test_del_like(liked_post, params, del_likes_url, get_likes_url, get_is_liked_url):
    post = liked_post["post_id"]
    params["item_id"] = post
    count = get_likes_count(post, params)
    response_api = requests.get(del_likes_url, params=params).json()
    count_ex = response_api["response"]["likes"]
    assert not get_is_liked(post, params), "Пост не удален из раздела 'Мне нравится' пользователя"
    assert count_ex == count - 1


@allure.story("Метод likes.add")
@allure.title("Проверка корректности ответа на запрос с неверным item_id")
@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.add
@pytest.mark.parametrize("item_id, msg, status",
                         [(-1, 'One of the parameters specified was missing or invalid: item_id should be greater or equal to 0', 100),
                          ('Foo', 'One of the parameters specified was missing or invalid: item_id not integer', 100),
                          (0, 'One of the parameters specified was missing or invalid: item_id is undefined', 100)])
def test_add_bad_item(params, item_id, msg, status, add_likes_url):
    params["item_id"] = item_id
    response = requests.get(add_likes_url, params=params).json()
    assert response.get("response") is None, "В ответе есть response, его не должно быть"
    assert response["error"]["error_code"] == status, f"Код ошибки неверный {response['error']['error_code']}, должен быть {status}"
    assert response["error"]["error_msg"] == msg, f"Cообщение об ошибке неверное, должно быть {msg}"


@allure.story("Метод likes.delete")
@allure.title("Проверка корректности ответа на запрос с неверным item_id")
@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.delete
@pytest.mark.parametrize("item_id, msg, status",
                         [(-1, 'One of the parameters specified was missing or invalid: item_id should be greater or equal to 0', 100),
                          ('Foo', 'One of the parameters specified was missing or invalid: item_id not integer', 100),
                          (0, 'One of the parameters specified was missing or invalid: item_id is undefined', 100)])
def test_del_bad_item(params, item_id, msg, status, del_likes_url):
    params["item_id"] = item_id
    response = requests.get(del_likes_url, params=params).json()
    assert response.get("response") is None, "В ответе есть response, его не должно быть"
    assert response["error"]["error_code"] == status, f"Код ошибки неверный {response['error']['error_code']}, должен быть {status}"
    assert response["error"]["error_msg"] == msg, f"Cообщение об ошибке неверное, должно быть {msg}"
