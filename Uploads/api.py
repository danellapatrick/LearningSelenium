# Request is used to test the API in selenium
# given all input details
# when - Submit the API
#then - validate a response
import json
import requests

url = "https://rahulshettyacademy.com/maps/api/place/add/json"
headers = {'Content-Type': 'application/json'}




def POST_DATA():

  params={'key':'qaclick123'}
  data={
    "location": {
      "lat": -38.383494,
      "lng": 33.427362
    },
    "accuracy": 50,
    "name": "Rahul Shetty",
    "phone_number": "(+91) 983 893 3937",
    "address": "29, side layout, cohen 09",
    "types": [
      "shoe park",
      "shop"
    ],
    "website": "http://google.com",
    "language": "French-IN"
  }

  r = requests.post(url,params=params,data=json.dumps(data), headers=headers)
  print(r.status_code)
  data1 = r.content
  resp = json.loads(data1)
  # print the resp
  print(resp)
  id=resp['place_id']
  # extract an element in the response
  print(id)
  return id

def GET_DATA():
  #place_id=POST_DATA()
  params={'key':'qaclick123','place_id':'2f0d13e0784308116089c397af446dd0'}
  r= requests.get(url,params=params, headers=headers)
  print(r.text)


GET_DATA()