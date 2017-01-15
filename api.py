#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_json import FlaskJSON, json_response
from controllers import Controllers

app = Flask(__name__)
FlaskJSON(app)

@app.route('/')
def hello():
    mensagem = 'API Canta Galo'
    return json_response(200, text=mensagem)

@app.route('/luz/<int:estado>')
def luz(estado):
    c = Controllers()
    negocio = c.managerluz(estado)
    return json_response(200, text= negocio)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
