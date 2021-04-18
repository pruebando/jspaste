
from .vares import *
from .errors import InvalidArgs, NotArgs, UnknownError
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
      raise UknownError("Uknown Error, Probably Server Does Not Respond")
    else:
     raise InvalidArgs(f"Need Str not {str(type(arguments))}")
    
     
       
