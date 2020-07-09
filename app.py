#!/usr/bin/env python
import base64
import os
import base64
import socket
from flask import Flask, request
from flask import render_template
from pystrich.qrcode import QRCodeEncoder

QR_DIR = os.path.join('qrcode-gen-img')

app = Flask(__name__)
app.config['QR_DIR'] = QR_DIR


@app.route('/')
def index():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return render_template("index.html", host_name=hostname, host_ip=hostip)


@app.route('/', methods=['POST'])
def qrcodegenerate():
    qrtext = request.form['text1']
    encoder = QRCodeEncoder(qrtext)
    encoder.save(os.path.join(app.config['QR_DIR'], 'test.png'), 3)
    image_src = os.path.join(app.config['QR_DIR'], 'test.png')
    data_uri = base64.b64encode(open(image_src, 'rb').read()).decode('utf-8')
    return render_template("generate.html", qr_img=data_uri)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
