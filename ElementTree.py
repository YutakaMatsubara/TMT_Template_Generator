'''
Created on Jun 3, 2016

@author: Jingxuan Wei
'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import Document

# create minidom-document
doc = Document()

# create child element for KnowledgeBase: Manifest, ThreatMetaData, GenericElements, StandardElements, ThreatCategories, ThreatTypes
# |KnowledgeBase
# |--Manifest
# |--ThreatMetaData
# |--GenericElements
# |--StandardElements
# |--ThreaCategories
# |--ThreatTypes
def create_KnowledgeBase(name, id, version, author):
    KnowledgeBase_Children = ["Manifest", "ThreatMetaData", "GenericElements", "StandardElements", "ThreatCategories", "ThreatTypes"]
    KnowledgeBase = doc.createElement("KnowledgeBase")
    KnowledgeBase.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    KnowledgeBase.setAttribute("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
    for child in KnowledgeBase_Children:
        KnowledgeBase_child = doc.createElement(child)
        # set attributes for Manifest
        if KnowledgeBase_child.nodeName == "Manifest":
            KnowledgeBase_child.setAttribute("name", name)
            KnowledgeBase_child.setAttribute("id", id)
            KnowledgeBase_child.setAttribute("version", version)
            KnowledgeBase_child.setAttribute("author", author)
        KnowledgeBase.appendChild(KnowledgeBase_child)
    return KnowledgeBase

# create child element for ThreatMetaDatum: Name, Label, HideFromUI, Values(Value), Id, AttributeType
# |ThreaMetaDatum
# |--Name
# |--Label
# |--HideFromUI
# |--Values
# |----Value
# |--Id
# |--AttributeType
def create_ThreatMetaDatum():
    ThreatMetaDatum_Children = ["Name", "Label", "HideFromUI", "Values", "Description", "Id", "AttributeType"]
    ThreatMetaDatum = doc.createElement("ThreatMetaDatum")
    for child in ThreatMetaDatum_Children:
        ThreatMetaDatum_child = doc.createElement(child)
        ThreatMetaDatum.appendChild(ThreatMetaDatum_child)
        if ThreatMetaDatum_child.nodeName == "Values":
            ThreatMetaDatum_child.appendChild(doc.createElement("Value"))
    return ThreatMetaDatum

# create child element for ThreatMetaData: IsPriorityUsed, IsStatusUsed, PropertiesMetaData
# |KnowledgeBase
# |--ThreatMetaData
# |----IsPriorityUsed
# |----IsStatusUsed
# |----PropertiesMetaData
def create_ThreatMetaData():
    ThreatMetaData_Children = ["IsPriorityUsed", "IsStatusUsed", "PropertiesMetaData"]
    ThreatMetaData = doc.createElement("ThreatMetaData")
    for child in ThreatMetaData_Children:
        ThreatMetaData_child = doc.createElement(child)
        if ThreatMetaData_child.nodeName == "PropertiesMetaData":
            ThreatMetaData_child.appendChild(create_ThreatMetaDatum())
        ThreatMetaData.appendChild(ThreatMetaData_child)
    return ThreatMetaData

# create child element for ElementType: "Name", "ID", "Description", "ParentElement", "Image", "Hidden", "Representation", "StrokeThickness", "ImageLocation", "Attributes"
# |ElementType
# |--Name
# |--ID
# |--Description
# |--ParentElement
# |--Image
# |--Hidden
# |--Representation
# |--StrokeThickness
# |--ImageLocation
# |--Attributes
def create_ElementType():
    ElementType_Children = {"Name", "ID", "Description", "ParentElement", "Image", "Hidden", "Representation", "StrokeThickness", "ImageLocation", "Attributes"}
    ElementType = doc.createElement("ElementType")
    for child in ElementType_Children:
        ElementType.appendChild(doc.createElement(child))
    return ElementType

# create child element for ThreatCategory: "Name", "Id", "ShortDescription
# |ThreatCategory
# |--Name
# |--Id
# |--ShortDescription
def create_ThreatCategory():
    ThreatCategory_Children = {"Name", "Id", "ShortDescription"}
    ThreatCategory = doc.createElement("ThreatCategory")
    for child in ThreatCategory_Children:
        ThreatCategory.appendChild(doc.createElement(child))
    return ThreatCategory

# create child element for ThreatType: "GenerationFilters", "Id", "ShortTitle", "Category", "RelatedCategory", "Description", "PropertiesMetaData"
# |ThreatType
# |--GenerationFilters
# |----Include
# |----Exclude
# |--Id
# |--ShortTitle
# |--Category
# |--RelatedCategory
# |--Description
# |--PropertiesMetaData
# |----ThreaMetaDatum
# |------Name
# |------Label
# |------HideFromUI
# |------Values
# |--------Value
# |------Id
# |------AttributeType
def create_ThreatType():
    ThreatType_Children = {"GenerationFilters", "Id", "ShortTitle", "Category", "RelatedCategory", "Description", "PropertiesMetaData"}
    ThreatType = doc.createElement("ThreatType")
    for child in ThreatType_Children:
        ThreatType_child = doc.createElement(child)
        ThreatType.appendChild(ThreatType_child)
        if ThreatType_child.nodeName == "GenerationFilters":
            ThreatType_child.appendChild(doc.createElement("Include"))
            ThreatType_child.appendChild(doc.createElement("Exclude"))
        if ThreatType_child.nodeName == "PropertiesMetaData":
            ThreatType.appendChild(create_ThreatMetaDatum())
    return ThreatType

# output xml documents to the console as well as to a file named: test.xml
def create_xml_file():
    # to console
    print (doc.toprettyxml(indent="    ", encoding="utf-8"))
    # to file
    f = open("test.xml", "w+")
    f.write(doc.toprettyxml(indent="    ", encoding="utf-8").decode("utf-8"))
    f.close