import requests
import xml.etree.ElementTree as ET

URL = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
NAMESPACE = {'dc': 'http://purl.org/dc/elements/1.1/'}

def fetch_xml():
    response = requests.get(URL)
    xml_tree = ET.fromstring(response.content)
    return xml_tree.findall('.//item')

