# CICD
CICD demo which sets up a basic Python Flask application, whose /healthcheck endpoint returns a JSON-based API.  The API returns the GIT commit hash, and commit comment, along with a version number.  

CICD pipeline runs:
  Unit tests in Python (mainly validity of the JSON returned by the API)
  Linting in Python
  Docker build
