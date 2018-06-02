import string


req = ['GET /','HEAD/','PUT/','DELETE/','CONNECT/','OPTIONS/','TRACE/']

def http(request):
  _req = ''
  for c in request:
     _req = _req + c
     if c == '/':
      break
  for el in req:
     if _req.strip("b'") == el:
        return True

   
