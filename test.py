# -*- coding: utf-8 -*-
from lxml import etree
 
def parseurlXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
                         
    root = etree.fromstring(xml)
    
    url_dict = {}
    urls = []
    for urls in root.getchildren():
        for elem in urls.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
                print(elem.tag + " => " + text)
                url_dict[elem.tag] = text
        if urls.tag == "link":
            urls.append(url_dict)
            url_dict = {}

    return urls


if __name__ == "__main__":
    parseurlXML("urls.xml")
