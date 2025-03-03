import requests
from json_parser import josn_parser
from xml_parser import xml_parser

if __name__ == '__main__':

    response = requests.get("https://api.restful-api.dev/objects")
    print("status code = ", response.status_code)

    if response.status_code != 200:
        raise Exception("could not connect to URL")
    else:
        josn_parser(response.json()[0])

# # xml parsing through URL
# response = requests.get("https://data.wa.gov/api/views/f6w7-q2d2/rows.xml?")
# if response.status_code == 200:
#     xml_parser(response.content)
