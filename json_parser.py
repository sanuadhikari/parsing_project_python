import json


def josn_parser(json_string):
    try:
        parse_data = json.loads(json_string)
        print(parse_data["name"])
        print(parse_data["age"])
        print(parse_data["city"])
    except json.JSONDecodeError as e:
        print(f"error parsing json:{e}")