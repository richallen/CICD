"""
A trivial server to respond with a JSON API
"""

import os
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
            "version": "local_run",
            "description": "",
            "lastcommitsha": "",
            "UTC": "",
        },
    ]
}

app = Flask(__name__)

def healthstring():
    """String response to healthcheck endpoint """

    if ('CI' in os.environ): # Must use CI flag in CI build

        if ('CI_DESCRIPTION' in os.environ):
          data[APPLICATION_NAME][0]["description"] = os.environ.get('CI_DESCRIPTION')
        else:
          data[APPLICATION_NAME][0]["description"] = 'No commit message provided'

        if ('CI_SHA' in os.environ):
          data[APPLICATION_NAME][0]["lastcommitsha"] = os.environ.get('CI_SHA')
        else:
          data[APPLICATION_NAME][0]["lastcommitsha"] = 'No sha provided'

        if ('CI_VERSION' in os.environ):
          data[APPLICATION_NAME][0]["version"] = os.environ.get('CI_VERSION')
        else:
          data[APPLICATION_NAME][0]["version"] = 'No version provided'

    else:
        data[APPLICATION_NAME][0]["description"] = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').rstrip()
        data[APPLICATION_NAME][0]["lastcommitsha"] = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').rstrip()

    data[APPLICATION_NAME][0]["UTC"] = datetime.now(timezone.utc).strftime(
        '%Y-%m-%dT%H:%M:%S'   # Request time
    )

    return json.dumps(data)


@app.route('/healthcheck')

def healthcheck():
    """HTTP response to healthcheck endpoint """
    return (Response(healthstring(),mimetype = "application/vnd.api+json"))

if __name__ == "__main__":
    print("Server started http://%s:%s"%(HOST_NAME, PORT))
    serve(TransLogger(app,setup_console_handler = True),host = HOST_NAME,port = PORT)
    print("Server stopped")
