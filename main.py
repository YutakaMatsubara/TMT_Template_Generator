import xml.dom.minidom
import uuid

from ElementTree import *

t_name = "Service Level"
t_id = str(uuid.uuid4())
t_version = "1.0.0.2"
t_author = "TMT Template Generator"

def main():
    KnowledgeBase = create_KnowledgeBase(t_name, t_id, t_version, t_author)
    doc.appendChild(KnowledgeBase)

    if KnowledgeBase.hasChildNodes():
        for node in KnowledgeBase.childNodes:
            if node.nodeName == "ThreatMetaData":
                ThreatMetaData = create_ThreatMetaData()
                node.appendChild(ThreatMetaData)
            elif node.nodeName == "GenericElements":
                GenericElementType = create_ElementType()
                node.appendChild(GenericElementType)
            elif node.nodeName == "StandardElements":
                StandardElementType = create_ElementType()
                node.appendChild(StandardElementType)
            elif node.nodeName == "ThreatCategories":
                ThreatCategory = create_ThreatCategory()
                node.appendChild(ThreatCategory)
            elif node.nodeName == "ThreatTypes":
                ThreatType = create_ThreatType()
                node.appendChild(ThreatType)

    create_xml_file()

if __name__ == "__main__":
    main();