#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
from flask import Flask, request, render_template
app = Flask(__name__)
# def index(request):
#     return web.Response(body='<span>Hello word!梵蒂冈!\u548c\u534e\u4e1c\u5e08\u8303!</span>\n'
#                              '<h1 style="color:#00ffff">gdfgdf</h1>'
#                         ,content_type='text/html',charset='utf-8')
@app.route('/', methods=['POST'])
def home():
    return render_template('home.html')
@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html', message="Welcome!!!")
@app.route('/signin', methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='123456':
         return render_template('login_ok.html', username=username)
    return render_template('form.html',messqge='Worng usernam or Password,please try agin',username=username)

if __name__ == '__main__':
    app.run('127.0.0.1',9000)

# @asyncio.coroutine
# def init(loop):
#     app= web.Application(loop= loop)
#     app.router.add_route('GET','/',signin_form)
#     srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
#     logging.info('server started at http://127.0.0.1:9000')
#
# loop= asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()