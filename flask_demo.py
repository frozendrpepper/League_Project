from flask import Flask, jsonify, request
import pickle
import numpy as np

app = Flask(__name__)

league_logistic = pickle.load(open('league_lr.pkl', 'rb'))

@app.route('/')
def say_hello():
    print('Welcome to League Predictor')

@app.route('/league', methods = ['POST'])
def make_predict():
    #get_json parses the incoming JSON request data and returns it.
    data = request.get_json(force=True)
    #The data that is stored inside 'data' is a dictionary. Now you want to
    #take each element and put it into a list
    predict_request = [data['gold'], data['xp'], data['cs'], data['ward'], data['wardkill'], data['dragon'],
                       data['herald'], data['champkill'], data['champassist'], data['tower'], data['inhibitor']]
    resize_shape = len(predict_request)
    #ML algorithms take np.array of specific size, so the following two lines
    #achieve that.
    predict_request = np.array(predict_request)
    predict_request = predict_request.reshape(1, resize_shape)
    
    #You want to return the probability of winning chance
    y_hat = league_logistic.predict_proba(predict_request)
    y_hat = y_hat[0][1]
    '''There is some issue turning np.array object to json object. Use .tolist() method for that
    Reference: https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable'''
    output = y_hat.tolist()
    '''From what I can understand, jsonify() method converts the result into a dictionary form
    results : output'''
    return jsonify(results = output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')