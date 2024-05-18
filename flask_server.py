"""
A trivial server to respond with a JSON API
"""

from datetime import datetime, timezone
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
        },
    ]
}

app = Flask(__name__)

def healthstring():
    """String response to healthcheck endpoint """
    data[APPLICATION_NAME][0]["UTC"] = datetime.now(timezone.utc).strftime(
        '%Y-%m-%dT%H:%M:%S'
    )
    return json.dumps(data)


@app.route('/healthcheck')

def healthcheck():
    """HTTP response to healthcheck endpoint """
    return (Response(healthstring(),mimetype = "application/vnd.api+json"))

if __name__ == "__main__":
    print("Server started http://%s:%s"%(HOST_NAME, PORT))
    serve(app,host = HOST_NAME,port = PORT)
    print("Server stopped")
