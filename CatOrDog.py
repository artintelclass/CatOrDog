import os
from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import json
import time
import base64
import numpy as np
import json
import matplotlib.pylab as plt
import time
#import sys
import csv

#sys.setdefaultencoding('utf-8')


#loading the model
basedir = os.path.abspath(os.path.dirname(__file__))
#with CustomObjectScope({'relu6': applications.mobilenet.relu6,'DepthwiseConv2D': applications.mobilenet.DepthwiseConv2D}):
#    model = load_model(os.path.join(basedir,'cat_dog_model.h5'))

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()
