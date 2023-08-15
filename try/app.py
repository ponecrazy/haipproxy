"""
-------------------------------------------------
    File Name       app
    Description     
    Author          Yifeng Peng
    date            2023-08-15
-------------------------------------------------
    change Activity
                    2023-08-15 create
                    
-------------------------------------------------
"""
from flask import (
    Flask, jsonify as flask_jsonify)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6001)






def jsonify(*args, **kwargs):
    response = flask_jsonify(*args, **kwargs)
    if not response.data.endswith(b"\n"):
        response.data += b"\n"
    return response



# web api uses robin strategy for proxy schedule, crawler client may implete
# its own schedule strategy
app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'reason': 'resource not found',
        'status_code': 404
    })


@app.errorhandler(500)
def not_found(e):
    return jsonify({
        'reason': 'internal server error',
        'status_code': 500
    })


@app.route("/proxy/get/<usage>")
def get_proxy(usage):
    # default usage is 'https'
    return jsonify({
        'resource': usage,
        'status_code': 200
    })


@app.route("/proxy/delete/<usage>/<proxy>")
def delete_proxy(usage, proxy):
    return jsonify({
        'result': 'ok',
        'status_code': 200
    })


@app.route("/pool/get/<usage>")
def get_proxies(usage):
    return jsonify({
        'resource': usage,
        'status_code': 200
    })
