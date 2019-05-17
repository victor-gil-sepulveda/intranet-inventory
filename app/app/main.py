import os
from eve import Eve

app = Eve(__name__, settings="/app/app/settings.py") #"#os.path.join("app", os.path.abspath('settings.py')))


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)

# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "Hello World from Flask in a uWSGI Nginx Docker container with \
#      Python 3.7 (from the example template)"
#
#
# if __name__ == "__main__":
#     # Only for debugging while developing
#     app.run(host='0.0.0.0', debug=True, port=80)