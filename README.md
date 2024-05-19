# CICD
CICD demo which sets up a basic Python Flask application, whose /healthcheck endpoint returns a JSON-based API.  The API returns the GIT commit hash, and commit comment, along with a version number.  

CICD pipeline runs:
- Unit tests in Python (mainly validity of the JSON returned by the API, e.g checks the commit hash must be alphanumeric hex)
- Linting in Python
- Docker build

Docker will only build if Unit tests and linting pass.

For local development use:
```
python3 -m pytest test_server.py
pylint test_server.py
pylint flask_server.py
./build-local.sh
docker run -i -p 9000:9000 -t ubuntu-serverhealth
```

Then `curl 127.0.0.1:9000/healthcheck` or, from a browser, `http:\\[machineIP]:9000/healthcheck` to exercise.

All of the above is packaged into the CICD pipeline in Github.
