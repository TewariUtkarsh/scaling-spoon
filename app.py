from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def index():

    return "Just a Flask App, updates in progress...."


if __name__ == '__main__':

    # host = '0.0.0.0'
    app.run(debug=True)
