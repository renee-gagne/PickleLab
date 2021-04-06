import pickle
import json

with open('model.pkl','rb') as f:
    pipe=pickle.load(f)

with open('newdata.py', 'r') as f:
    testdata=json.load(f)

pred=pipe.predict_proba([testdata])
print(pred)
