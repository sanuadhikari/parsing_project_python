from json_parser import josn_parser
from xml_parser import xml_parser

if __name__ == '__main__':
    xml = '''<root>
                <person>
                    <name>John</name>
                    <age>30</age>
                </person>
                <person>
                    <name>Jane</name>
                    <age>25</age>
                </person>
              </root>'''

    json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

    xml_parser(xml)
    josn_parser(json_string)
