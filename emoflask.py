from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import joblib
import json


app = Flask(__name__)
api = Api(app)

class emotionText(Resource):
    def post(self):
        pipeLine = joblib.load("emotion_classifier_pipe_lr_03_june_2021.pkl")

        mess = request.form.get("message")

        ge = pipeLine.predict([mess])
        print(ge[0])
        return {'emotion':str(ge[0])}



api.add_resource(emotionText,'/emotion')
app.run(host='0.0.0.0', debug=True)
