#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from random import *
import string
import functions.prosImage as prosImage
import functions.playSound as playSound
import functions.utils as utils
app = Flask(__name__)

@app.route('/api/')
def hello_world():
    return "Hello World!"


@app.route("/api/testpost", methods=['POST'])
def hello():
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
    base64_png = request.form['image']
    img_array = utils.base64toCV2(base64_png)

    processedImg = prosImage.cannyImage(img_array)
    resultImage = utils.CV2toBase64(processedImg)

    calcedRGB = prosImage.calcRGB(img_array)

    response = {
        'iamge': resultImage,
        'red'   : calcedRGB[0],
        'green' : calcedRGB[1],
        'blue'  : calcedRGB[2]
    }
    return jsonify(response)

@app.route('/api/makeMusic', methods=['GET'])
def makeMusic():
    pm = playSound.makeSound()

    music = utils.PMtoBase64(pm)

    response = {
        'music' : music
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
