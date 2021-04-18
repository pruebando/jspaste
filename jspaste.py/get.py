from .vares import *
from .errors import InvalidArgs, NotArgs, UnknownError
import requests

def get(key):
    if isinstance(key, str):
        a = requests.get(f"{BaseUrl}documents/{key}")
        if a.status_code == 404:
            raise InvalidArgs("Invalid Key")
        class document:
            data = a.json()["data"]
            content = data
            key = a.json()["key"]
            link = BaseUrl + key
            url = link
        return document
    else:
        InvalidArgs(f"Key needs to be str not {str(type(key))}")
