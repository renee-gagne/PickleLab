##Requests library

import requests
import json

#Load the test data
with open('newdata.py', 'r') as f:
    testdata=json.load(f)

#r=requests.get('http://127.0.0.1:5000/predict')
r=requests.post('http://127.0.0.1:5000/predict', json={'newdata':testdata})
data= r.json()
prediction=data['prediction']
#print(prediction)
print(f'Goood day to you. The prediction is: {prediction}')
