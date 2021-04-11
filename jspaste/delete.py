from errors import *
from vares import *
import errors 
import vares 
import json
import requests

def delete(key, secret):
 if not isinstance(key, str):
     raise errors.InvalidArgs(f"key needs to be str not {str(type(key))}")
 else:
  if not isinstance(secret, str):
      raise errors.InvalidArgs(f"secret needs to be str not {str(type(secret))}")
  else:
   obtain = requests.get(f"{BaseUrl}documents/{key}")
   if obtain.status_code == 404:
       raise errors.InvalidArgs("Invalid key")
   else:
       headers = {"Secret": f"{secret}"}
       
       ao = requests.post(f"{BaseUrl}documents/{key}/delete", headers = headers)
       class deleted():
           key = ao.json()["key"]
           deleted = ao.json()["eliminado"]
       if ao.status_code == 400:
           raise errors.InvalidArgs("invalid secret code")
          
