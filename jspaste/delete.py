from .vares import *
from .errors import InvalidArgs, NotArgs, UnknownError
import requests

import json


def delete(key, secret):
 if not isinstance(key, str):
     raise InvalidArgs(f"key needs to be str not {str(type(key))}")
 else:
  if not isinstance(secret, str):
      raise InvalidArgs(f"secret needs to be str not {str(type(secret))}")
  else:
   obtain = requests.get(f"{BaseUrl}documents/{key}")
   if obtain.status_code == 404:
       raise InvalidArgs("Invalid key")
   else:
       headers = {"Secret": f"{secret}"}
       
       ao = requests.post(f"{BaseUrl}documents/{key}/delete", headers = headers)
       class deleted():
           key = ao.json()["key"]
           deleted = ao.json()["eliminado"]
       if ao.status_code == 400:
           raise InvalidArgs("invalid secret code")
          
