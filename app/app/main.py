import os
from eve import Eve

app = Eve(__name__, settings="/app/app/settings.py") #"#os.path.join("app", os.path.abspath('settings.py')))


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,If-Match')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


def on_inserted_item(items):
    print("INSERTED ITEM", items)


app.on_inserted_item += on_inserted_item

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
