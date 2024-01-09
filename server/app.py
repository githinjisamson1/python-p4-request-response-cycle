#!/usr/bin/env python3

'''
import module
when a cient makes a request, Flask generates request and application contexts
'''
from flask import Flask, request, current_app, g, make_response, redirect, abort
import os

# !initialize
app = Flask(__name__)


# !request hook
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())


# !routes and views
@app.route("/")
def index():
    host = request.headers.get("Host")
    app_name = current_app.name
    
    response_body = f'''<h1>The host for this page is {host}</h1>
                <h2>The name of this application is {app_name}</h2>
                <h3>The path of this application on the user's device is {g.path}</h3>
              '''

    status_code = 202
    headers = {}

    # 3 args
    return make_response(response_body, status_code, headers)

# !redirect/pass URL to relocate to
@app.route('/reginald-kenneth-dwight')
def name():
    return redirect('names.com/elton-john')

# !abort
@app.route("/<stage_name>")
def get_name(stage_name):
    match = session.query("StageName").filter(StageName.name == stage_name)[0]

    if not match:
        abort(404)

    response_body = f'<h1>{stage_name} is an existing stage name!</h1>'
    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)


# execute only if we run this file/not if imported
if __name__ == '__main__':
    # re-run upon change
    app.run(port=5555, debug=True)

'''
If you're testing request for a specific app outside of any views, you will have to generate this context manually.

from app import app
from flask import request, current_app

request_context = app.test_request_context()
request_context.push()
request.url

app_context =  app.app_context()
app_context.push()
current_app.name

request_context = app.request_context()
request_contet.push()
request.url

NOTE: If you are working in a debugging shell, it is a good idea to clear out your request_context object with its pop() method before moving onto a new request.

app_context makes available:
current_app: instance of active app
g: for temporary storage/reset upon each request

request_context makes available:
request: actual request
session: dictionary to store values to be remembered btwn requests

request dispatching:
determining view function to run
check application url map
url/routes are mapped to specific view functions
app.url_map()

methods to act on request obj:
get_data
get_json
is_secure

variables made available by request:
endpoint
method
host
URL
environ

request hooks/implemented as decorators:
@app.before_request: run before each request
@app.before_first_request: before first request
@app.after_request: after each request, only when exceptions have been handled
@app.tear-down_request: after each request, regardless of whether exceptions have been handled

ipdb> app.url_map

creating responses/3 args:
response
status code
headers dictionary
return "Hello", 202, {key:value}

OR
return make_response(response_body, status_code, headers)

special responses
pass URL of relocated resource
@app.route('/reginald-kenneth-dwight')
def index():
    return redirect('names.com/elton-john')


'''
