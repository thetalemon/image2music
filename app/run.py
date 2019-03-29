#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(__file__)


from flask import Flask, render_template, jsonify, request
from random import *
import string
import sys
sys.path.insert(0, '/var/www')
from functions.prosImage import *
from functions.playSound import *
from functions.convertData import *

app = Flask(__name__,
                    static_folder = "./dist/static",
                                template_folder = "./dist")

@app.route('/api/')
def hello_world():
    return "Hello World!"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
        return render_template("index.html")

@app.route("/api/testpost", methods=['POST'])
def double_num():
    response = {
        "result": int(request.json["val1"].split()[0])*2
    }
    return jsonify(response)

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/cannyFile', methods=['POST'])
def upload():
    print("canny!")
    base64_png = request.form['image']
    img_array = functions.convertData.base64toCV2(base64_png)

    processedImg = functions.prosImage.cannyImage(img_array)
    resultImage = functions.convertData.CV2toBase64(processedImg)

    calcedRGB = functions.prosImage.calcRGB(img_array)

    response = {
        'iamge': resultImage,
        'red'   : calcedRGB[0],
        'green' : calcedRGB[1],
        'blue'  : calcedRGB[2]
    }
    return jsonify(response)

@app.route('/api/makeMusic', methods=['GET'])
def makeMusic():
    print("makeMusic!")
    pm = functions.playSound.makeSound()

    music = functions.convertData.PMtoBase64(pm)

    response = {
        'music' : music
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
