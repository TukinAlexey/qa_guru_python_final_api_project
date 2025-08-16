register_successful_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "token": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "token"
  ]
}

register_unsuccessful_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}


register_successful_request_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "email": {
      "type": "string"
    },
    "password": {
      "type": "string"
    }
  },
  "required": [
    "email",
    "password"
  ]
}


register_unsuccessful_request_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "email": {
      "type": "string"
    }
  },
  "required": [
    "email"
  ]
}