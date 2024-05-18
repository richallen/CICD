#! /usr/bin/python3
import datetime
import json
from flask import Flask
from waitress import serve
from flask import Response

applicationName = "Application Test 1"
hostName = "0.0.0.0"
PORT = 9000

data = {
    applicationName: [
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
    data[applicationName][0]["UTC"] = datetime.datetime.now(datetime.UTC).strftime(
        '%Y-%m-%d %H:%M:%S'
    )
    return (Response(json.dumps(data),mimetype = "application/vnd.api+json"))

if __name__ == "__main__":
  print("Server started http://%s:%s"%(hostName, PORT))
  serve(app,host = hostName,port = PORT)
  print("Server stopped")
