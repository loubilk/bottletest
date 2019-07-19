#!/usr/bin/env python
"""
    A simple application that shows how Bottle and jQuery get along.

    :copyright: (c) 2015 by Oz Nahum Tiram.
    :license: BSD, see LICENSE for more details.

    Inspired by the same example given in Flask
    :copyright: (c) 2015 by Armin Ronacher.
"""
from bottle import route, run, debug, template, request, static_file
import os
import json
import logging
from django.core.paginator import Paginator

# logging.basicConfig(filename='example.log',level=logging.DEBUG)
my_dir = os.getcwd()

@route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.params.get('a', 0, type=int)
    b = request.params.get('b', 0, type=int)
    return json.dumps({'result': a+b})


@route('/foo/:no')
def bar(no):
    return template('index.tpl', request=request)


@route('/')
def index():
    # print("hola")
    with open('generated.json') as json_file:
        data = json.load(json_file)

        # print(data)
    data2 = []
    x=0
    y=0
    for i in data:
        x+=1
        if i['isActive']==True:
            data2.append(i)
            y+=1

    
    print(type(data2))
    print(data2)
    print(x,y)
    return template('index.tpl', request=request, data=data2)

@route('/static/<filepath:path>')
def serve_static_content(filepath):
    my_root = os.path.join(my_dir, 'static')
    logging.info("my_root")
    return static_file(filepath, root=my_root)


run(debug=True, reloader=True, port=8080)
