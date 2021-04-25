from flask import Flask, request
import pickle
app = Flask(__name__)

with open('model.pkl','rb') as f:
    pipe=pickle.load(f)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/json_test')
def json_test():
    return{'prediction':0.5}


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        the_data = request.get_json(force=True)
        newdata=the_data['newdata']
        prediction=pipe.predict([newdata])
        return{'prediction' : prediction.tolist()}
        #print(f'Good day to you. The prediction for the data is: {'prediction' : prediction.tolist()}')
