import pytest
from config import API_GET_LIKES, ACCESS_TOKEN, API_VERSION, VK_USER_ID, ITEM_ID


@pytest.fixture
def params():
    data = {
        "type": "post",
        "v": API_VERSION,
        'user_id': VK_USER_ID,
        'item_id': ITEM_ID
    }
    return data


@pytest.fixture(scope="session")
def get_likes_url():
    return API_GET_LIKES


@pytest.fixture(scope="session")
def headers():
    headers = {'Authorization': ACCESS_TOKEN}
    return headers
