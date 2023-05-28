import pytest
from config import API_GET_LIKES, ACCESS_TOKEN, API_VERSION, VK_USER_ID, ITEM_ID, API_ADD_LIKES, API_DEL_LIKES
import os
import time
import yaml

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
        """Ограничение количества запросов"""
        time.sleep(0.5)

    request.addfinalizer(fin)
    return data


@pytest.fixture(scope="session")
def get_likes_url():
    return API_GET_LIKES

@pytest.fixture(scope="session")
def add_likes_url():
    return API_ADD_LIKES

@pytest.fixture(scope="session")
def del_likes_url():
    return API_DEL_LIKES

'''Фикстура для проверки параметризации из файла yaml'''
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