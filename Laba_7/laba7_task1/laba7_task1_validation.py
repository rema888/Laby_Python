import json
from jsonschema import validate, ValidationError

schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "База данных фильмов",
  "type": "object",
  "properties":
  {
    "movies":
    {
      "type": "array",
      "items":
      {
        "type": "object",
        "properties":
        {
          "title":
          {
            "type": "string"
          },
          "year":
          {
            "type": "integer",
            "minimum": 1900,
            "maximum": 2025
          },
          "cast":
          {
            "type": "array",
            "items":
            {
              "type": "object",
              "properties":
              {
                "name":
                {
                  "type": "string"
                },
                "role":
                {
                  "type": "string"
                }
              },
              "required": ["name", "role"]
            }
          }
        },
        "required": ["title", "year", "cast"]
      }
    }
  },
  "required": ["movies"]
}

def validate_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        try:
            validate(instance=data, schema=schema)
            print("Файл прошел валидацию")
        except ValidationError as e:
            print("Ошибка валидации:", e.message)

validate_json('json files/ex1.json') # Файл прошел валидацию
validate_json('json files/not_valid_ex1.json') # Ошибка валидации: 'year' is a required property