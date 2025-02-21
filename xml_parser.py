import xml.etree.ElementTree as ET


def xml_parser(xml_data):
    root = ET.fromstring(xml_data)
    # Use a breakpoint in the code line below to debug your script.
    for person in root.findall("person"):
        name = person.find("name").text
        age = person.find("age").text
        print(name, age)
