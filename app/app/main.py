import os
from eve import Eve

app = Eve(__name__, settings="/app/app/settings.py") #"#os.path.join("app", os.path.abspath('settings.py')))

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