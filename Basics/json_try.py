import json
import numpy as np
import pandas as pd

data='''{
"dashboard": {
"purchaseAmount": 910,
"website": "rahulshettyacademy.com"
},
"courses": [
{
"title": "Selenium Python",
"price": 50,
"copies": 6
},
{
"title": "Cypress",
"price": 40,
"copies": 4
},
{
"title": "RPA",
"price": 45,
"copies": 10
}
]
}'''

data1= json.loads(data)
courses=len(data1['courses'])
print("The number of courses are:",courses)
purchase_amount = data1['dashboard']['purchaseAmount']
print("The Purchase Amount is:",purchase_amount)
for i in data1['courses']:
    print(i['title'])
    if i['title']=='RPA':
        print( "The number of copies:",i['copies'])
list1=[]
for k in data1['courses']:
    list1.append(k['price'])
print(np.sum(list1))