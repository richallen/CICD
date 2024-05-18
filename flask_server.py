"""
A trivial server to respond with a JSON API
"""

from datetime import datetime, timezone
import json
import logging.config
import logging
import subprocess
from flask import Flask
from flask import Response
from waitress import serve
from paste.translogger import TransLogger

APPLICATION_NAME = "Application Test 1"
HOST_NAME = "0.0.0.0"
PORT = 9000

logging.basicConfig(filename = './server.log',encoding='utf-8',level = logging.DEBUG)
logger = logging.getLogger('waitress')

data = {
    APPLICATION_NAME: [
        {
            "version": "1.0",
            "description": "",
            "lastcommitsha": "",
            "UTC": "",
        },
    ]
}

app = Flask(__name__)

def healthstring():
    """String response to healthcheck endpoint """
    data[APPLICATION_NAME][0]["description"] = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').rstrip()
    data[APPLICATION_NAME][0]["lastcommitsha"] = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').rstrip()
    data[APPLICATION_NAME][0]["UTC"] = datetime.now(timezone.utc).strftime(
        '%Y-%m-%dT%H:%M:%S'
    )
    print (data)
    return json.dumps(data)


@app.route('/healthcheck')

def healthcheck():
    """HTTP response to healthcheck endpoint """
    return (Response(healthstring(),mimetype = "application/vnd.api+json"))

if __name__ == "__main__":
    print("Server started http://%s:%s"%(HOST_NAME, PORT))
    serve(TransLogger(app,setup_console_handler=True),host = HOST_NAME,port = PORT)
    print("Server stopped")
