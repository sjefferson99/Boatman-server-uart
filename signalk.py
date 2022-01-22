# sender.py
import json
import uuid

def put_light_1(value):

  requestid = str(uuid.uuid4())
  print("Request ID: {}".format(requestid))
  path = "/vessels/self/environment/inside/lights/1"
  print("Path: {}".format(path))
  print("Value: {}".format(value))
  signalk = json.dumps({"requestId" : requestid, "put": {"path": path, "value": value}})
  print(signalk)
  return signalk