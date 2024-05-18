"""
A trivial server to respond with a JSON API
"""

import datetime
import json
from flask import Flask
from flask import Response
from waitress import serve

APPLICATION_NAME = "Application Test 1"
HOST_NAME = "0.0.0.0"
PORT = 9000

data = {
    APPLICATION_NAME: [
        {
            "version": "1.0",
            "description": "pre-interview technical test",
            "lastcommitsha": "abc57858585",
            "UTC": "",
        }
    ]
}

app = Flask(__name__)

@app.route('/healthcheck')

def healthcheck():
    """String response to healthcheck endpoint """
    data[APPLICATION_NAME][0]["UTC"] = datetime.datetime.now(datetime.UTC).strftime(
        '%Y-%m-%d %H:%M:%S'
    )
    return (Response(json.dumps(data),mimetype = "application/vnd.api+json"))

if __name__ == "__main__":
    print(f"Server started http://%s:%s"%(HOST_NAME, PORT))
    serve(app,host = HOST_NAME,port = PORT)
    print("Server stopped")
