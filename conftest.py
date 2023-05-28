import pytest
from config import API_GET_LIKES, API_IS_LIKED, ACCESS_TOKEN, API_VERSION, VK_USER_ID, ITEM_ID, API_ADD_LIKES, API_DEL_LIKES, POSTS
import os
import time
import yaml
from random import choice
from utils import get_is_liked, delete_like, add_like, get_likes_count


@pytest.fixture
def params(request):
    data = {
        "type": "post",
        "v": API_VERSION,
        "access_token": ACCESS_TOKEN,
        'user_id': VK_USER_ID,
        'item_id': ITEM_ID
    }

    def fin():
        """Ограничение количества запросов, иначе код ошибки 6, слишком много запросов в секунду."""
        time.sleep(2)

    request.addfinalizer(fin)
    return data


@pytest.fixture(scope="session")
def get_likes_url():
    return API_GET_LIKES


@pytest.fixture(scope="session")
def get_is_liked_url():
    return API_IS_LIKED


@pytest.fixture(scope="session")
def add_likes_url():
    return API_ADD_LIKES


@pytest.fixture(scope="session")
def del_likes_url():
    return API_DEL_LIKES


"""Фикстура для проверки параметризации из файла yaml"""


def pytest_generate_tests(metafunc):

    # Проверка наличия аргумента multi_type
    if 'multi_type' not in metafunc.fixturenames:
        return

    # Директория текущего файла
    dir_path = os.path.dirname(os.path.abspath(metafunc.module.__file__))

    # Путь к файлу с данными
    file_path = os.path.join(dir_path, metafunc.function.__name__ + '.yaml')

    with open(file_path) as f:
        test_cases = yaml.full_load(f)

    # Проверка неправильной загрузки и/или пустого файла
    if not test_cases:
        raise ValueError("Test cases not loaded")

    return metafunc.parametrize("multi_type, item_id", test_cases)


"""Так как нет возможности генерить тестовые данные, используются реальные айди постов"""


@pytest.fixture
def not_liked_post(params):
    post = choice(POSTS)
    if get_is_liked(post, params):
        likes = delete_like(post, params)
    else:
        likes = get_likes_count(post, params)
    return {"post_id": post, "likes": likes}


@pytest.fixture
def liked_post(params):
    post = choice(POSTS)
    if not get_is_liked(post, params):
        likes = add_like(post, params)
    else:
        likes = get_likes_count(post, params)
    return {"post_id": post, "likes": likes}
