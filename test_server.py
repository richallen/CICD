"""
Unit test for flask_server.py
"""

import unittest
import json
import jsonschema
import flask_server

schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "Application Test 1": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "version": {
              "type": "string",
              # Actually version seems to be a description, not numbers.  "pattern": "^[0-9.]+$" # digits and dots
            },
            "description": {
              "type": "string"
            },
            "lastcommitsha": {
              "type": "string",
              "pattern": "^[0-9a-f]+$" # lowercase hex
            },
            "UTC": {
              "type": "string",
              "format": "date-time" # RFC 339 sect 5.6
            }
          },
          "required": [
            "version",
            "description",
            "lastcommitsha",
          ],
        }
      ],
      "minItems":1,
      "maxItems":1,
    }
  },
  "required": [
    "Application Test 1"
  ]
}

class JSONTest(unittest.TestCase):
    """ All necessary tests for flask_server """
    def test(self):
        """ Validate the string against a JSON schema """
        reply=json.loads(flask_server.healthstring())

        status = True
        try:
            jsonschema.validate(instance = reply,schema = schema)
        except jsonschema.exceptions.ValidationError:
            status = False
        self.assertTrue(status)

if __name__ == '__main__':
    unittest.main()
