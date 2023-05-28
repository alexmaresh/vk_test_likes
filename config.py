import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.vk.com/method/likes."
API_VERSION = "5.131"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("STANDALONE")
VK_USER_ID = os.getenv("VK_USER_ID")
ITEM_ID = os.getenv("ITEM_ID")

API_GET_LIKES = API_URL + "getList"
API_IS_LIKED = API_URL + "isLiked"
API_ADD_LIKES = API_URL + "add"
API_DEL_LIKES = API_URL + "delete"

POSTS = ["1291", "1273", "1228"]
