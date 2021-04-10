from errors import *
import errors
from vares import *
import vares
import requests     


      class response():
       response = requests.post(BaseUrl, data=Content)
       key = json.loads(response)["key"]
     except:
      raise UknownError("Uknown Error, Probably Server Does Not Respond")
    else:
     raise InvalidArgs(f"Need Str not {str(type(arguments))}")
    
     
def GetKey(Response):
    if not isinstance(Response, requests.models.):
        raise InvalidArgs(f"You need to put a dict, not a {str(type(Response))}")
    else:
        try:
            return Response["key"]
        except: 
            raise UknownError("Uknown Error")
       