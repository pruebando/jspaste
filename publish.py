from errors import *
from vares import *
import errors
import vares
import requests

def publish(arguments):
    if isinstance(arguments, str):
     Content = f"/*Made With Jspaste.py Created By {Creator}*/\n \n{arguments}"
     try:
      class response:
       response = requests.post(BaseUrl+ "documents", data=Content.encode('utf-8'))
       key = response.json()["key"]
       secret = response.json()["secret"]
       link = BaseUrl + key
       url = link 
      return response
     except:
      raise
      raise errors.UknownError("Uknown Error, Probably Server Does Not Respond")
    else:
     raise errors.InvalidArgs(f"Need Str not {str(type(arguments))}")
    
     
       