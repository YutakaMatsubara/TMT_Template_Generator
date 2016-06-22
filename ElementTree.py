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

# create child element for Values: value
# |Values
# |--value
# |--value
# |--value
# |--...
def create_Values(*values):
    Values = doc.createElement("Values")
    for v in values:
        if v == "":
            return ""
        elif v == "Not Set":
            Values.appendChild(doc.createElement("Value"))
            return Values
        else:
            Value = doc.createElement("Value")
            Value.appendChild(doc.createTextNode(str(v)))
            Values.appendChild(Value)
    return Values

# create child element for ThreatMetaDatum: Name, Label, HideFromUI, Values(Value), Id, AttributeType
# |ThreaMetaDatum
# |--Name
# |--Label
# |--HideFromUI
# |--Values
# |----Value
# |--Id
# |--AttributeType
def create_ThreatMetaDatum(name, label, hide_from_ui, values, description, id, attributes_type):
    ThreatMetaDatum_Children = ["Name", "Label", "HideFromUI", "Values", "Description", "Id", "AttributeType"]
    ThreatMetaDatum = doc.createElement("ThreatMetaDatum")
    for child in ThreatMetaDatum_Children:
        ThreatMetaDatum_child = doc.createElement(child)
        if ThreatMetaDatum_child.nodeName == ThreatMetaDatum_Children[0] and name != "":
            ThreatMetaDatum_child.appendChild(doc.createTextNode(name))
            ThreatMetaDatum.appendChild(ThreatMetaDatum_child)
        if ThreatMetaDatum_child.nodeName == ThreatMetaDatum_Children[1] and label != "":
            ThreatMetaDatum_child.appendChild(doc.createTextNode(label))
            ThreatMetaDatum.appendChild(ThreatMetaDatum_child)
        if ThreatMetaDatum_child.nodeName == ThreatMetaDatum_Children[2] and hide_from_ui != "":
            ThreatMetaDatum_child.appendChild(doc.createTextNode(hide_from_ui))
            ThreatMetaDatum.appendChild(ThreatMetaDatum_child)
        if ThreatMetaDatum_child.nodeName == ThreatMetaDatum_Children[3] and values != "":
            ThreatMetaDatum.appendChild(values)
        if ThreatMetaDatum_child.nodeName == ThreatMetaDatum_Children[4] and description != "":
            ThreatMetaDatum_child.appendChild(doc.createTextNode(description))
            ThreatMetaDatum.appendChild(ThreatMetaDatum_child)
        if ThreatMetaDatum_child.nodeName == ThreatMetaDatum_Children[5] and id != "":
            ThreatMetaDatum_child.appendChild(doc.createTextNode(id))
            ThreatMetaDatum.appendChild(ThreatMetaDatum_child)
        if ThreatMetaDatum_child.nodeName == ThreatMetaDatum_Children[6] and attributes_type != "":
            ThreatMetaDatum_child.appendChild(doc.createTextNode(attributes_type))
            ThreatMetaDatum.appendChild(ThreatMetaDatum_child)
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
        ThreatMetaData.appendChild(ThreatMetaData_child)
    return ThreatMetaData

# create child element for GenericElementType: "Name", "ID", "Description", "ParentElement", "Image", "Hidden", "Representation", "StrokeThickness", "ImageLocation", "Attributes"
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
def create_GenericElementType(name, id, description, parent_element, image, hidden, representation, stroke_thickness, image_location, attributes):
    ElementType_Children = ["Name", "ID", "Description", "ParentElement", "Image", "Hidden", "Representation", "StrokeThickness", "ImageLocation", "Attributes"]
    ElementType = doc.createElement("ElementType")
    for child in ElementType_Children:
        ElementType_child = doc.createElement(child)
        if ElementType_child.nodeName == ElementType_Children[0]:
            if name != "":
                ElementType_child.appendChild(doc.createTextNode(name))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[1]:
            if id != "":
                ElementType_child.appendChild(doc.createTextNode(id))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[2]:
            if description != "":
                ElementType_child.appendChild(doc.createTextNode(description))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[3]:
            if parent_element != "":
                ElementType_child.appendChild(doc.createTextNode(parent_element))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[4]:
            if image != "":
                ElementType_child.appendChild(doc.createTextNode(image))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[5]:
            if hidden != "":
                ElementType_child.appendChild(doc.createTextNode(hidden))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[6]:
            if representation != "":
                ElementType_child.appendChild(doc.createTextNode(representation))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[7]:
            if stroke_thickness != "":
                ElementType_child.appendChild(doc.createTextNode(stroke_thickness))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[8]:
            if image_location != "":
                ElementType_child.appendChild(doc.createTextNode(image_location))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[9]:
            if attributes != "":
                ElementType_child.appendChild(doc.createTextNode(attributes))
            ElementType.appendChild(ElementType_child)
    return ElementType

def create_StandardElementType(name, id, description, parent_element, image, image_stream, hidden, representation, stroke_thickness, image_location, attributes):
    ElementType_Children = ["Name", "ID", "Description", "ParentElement", "Image", "ImageStream", "Hidden", "Representation", "StrokeThickness", "ImageLocation", "Attributes"]
    ElementType = doc.createElement("ElementType")
    for child in ElementType_Children:
        ElementType_child = doc.createElement(child)
        if ElementType_child.nodeName == ElementType_Children[0]:
            if name != "":
                ElementType_child.appendChild(doc.createTextNode(name))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[1]:
            if id != "":
                ElementType_child.appendChild(doc.createTextNode(id))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[2]:
            if description != "":
                ElementType_child.appendChild(doc.createTextNode(description))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[3]:
            if parent_element != "":
                ElementType_child.appendChild(doc.createTextNode(parent_element))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[4]:
            if image != "":
                ElementType_child.appendChild(doc.createTextNode(image))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[5]:
            if image_stream != "":
                ElementType_child.appendChild(doc.createTextNode(image_stream))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[6]:
            if hidden != "":
                ElementType_child.appendChild(doc.createTextNode(hidden))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[7]:
            if representation != "":
                ElementType_child.appendChild(doc.createTextNode(representation))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[8]:
            if stroke_thickness != "":
                ElementType_child.appendChild(doc.createTextNode(stroke_thickness))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[9]:
            if image_location != "":
                ElementType_child.appendChild(doc.createTextNode(image_location))
            ElementType.appendChild(ElementType_child)
        if ElementType_child.nodeName == ElementType_Children[10]:
            if attributes != "":
                ElementType_child.appendChild(doc.createTextNode(attributes))
            ElementType.appendChild(ElementType_child)
    return ElementType

# create child element for ThreatCategory: "Name", "Id", "ShortDescription
# |ThreatCategory
# |--Name
# |--Id
# |--ShortDescription
def create_ThreatCategory(name, id, short_description):
    ThreatCategory_Children = ["Name", "Id", "ShortDescription"]
    ThreatCategory = doc.createElement("ThreatCategory")
    for child in ThreatCategory_Children:
        ThreatCategory_child = doc.createElement(child)
        if ThreatCategory_child.nodeName == ThreatCategory_Children[0]:
            if name != "":
                ThreatCategory_child.appendChild(doc.createTextNode(name))
            ThreatCategory.appendChild(ThreatCategory_child)
        if ThreatCategory_child.nodeName == ThreatCategory_Children[1]:
            if id != "":
                ThreatCategory_child.appendChild(doc.createTextNode(id))
            ThreatCategory.appendChild(ThreatCategory_child)
        if ThreatCategory_child.nodeName == ThreatCategory_Children[2]:
            if short_description != "":
                ThreatCategory_child.appendChild(doc.createTextNode(short_description))
            ThreatCategory.appendChild(ThreatCategory_child)
    return ThreatCategory

def AND(and1, and2):
    AND = and1 + " and " + and2
    return AND

def OR(or1, or2):
    OR = or1 + " or " + or2
    return OR

def create_IncludeStatement(id1, id2):
    id1 = "'" + id1 + "'"
    id2 = "'" + id2 + "'"

    source = "source is"
    target = "target is"

    Include1 = "(" + AND(source + " " + id1, target + " " + id2) + ")"
    Include2 = "(" + AND(source + " " + id2, target + " " + id1) + ")"
    Include = OR(Include1, Include2)

    return Include

# create child element for ThreatType -> GenerationFilters: "Include", "Exclude" 
# |ThreatType
# |--GenerationFilters
# |----Include
# |----Exclude
def create_GenerationFilters(include, exclude):
    GenerationFilters = doc.createElement("GenerationFilters")
    GenerationFilters.appendChild(doc.createElement("Include"))
    GenerationFilters.appendChild(doc.createElement("Exclude"))

    for node in GenerationFilters.childNodes:
        if node.nodeName == "Include" and include != "":
            node.appendChild(doc.createTextNode(include))
        elif node.nodeName == "Exclude" and exclude != "":
            node.appendChild(doc.createTextNode(exclude))

    return GenerationFilters

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
def create_ThreatType(generation_filters, id, short_title, category, related_category, description, properties_meta_data):
    ThreatType_Children = ["GenerationFilters", "Id", "ShortTitle", "Category", "RelatedCategory", "Description", "PropertiesMetaData"]
    ThreatType = doc.createElement("ThreatType")
    for child in ThreatType_Children:
        if child == "GenerationFilters":
            ThreatType.appendChild(generation_filters)
        else:
            ThreatType_child = doc.createElement(child)
            ThreatType.appendChild(ThreatType_child)
            if ThreatType_child.nodeName == ThreatType_Children[1] and id != "":
                ThreatType_child.appendChild(doc.createTextNode(id))
            elif ThreatType_child.nodeName == ThreatType_Children[2] and short_title != "":
                ThreatType_child.appendChild(doc.createTextNode(short_title))
            elif ThreatType_child.nodeName == ThreatType_Children[3] and category != "":
                ThreatType_child.appendChild(doc.createTextNode(category))
            elif ThreatType_child.nodeName == ThreatType_Children[4] and related_category != "":
                ThreatType_child.appendChild(doc.createTextNode(related_category))
            elif ThreatType_child.nodeName == ThreatType_Children[5] and description != "":
                ThreatType_child.appendChild(doc.createTextNode(description))

    return ThreatType

# output xml documents to the console as well as to a file named: test.xml
def create_xml_file():
    # to console
    print (doc.toprettyxml(indent="  ", encoding="utf-8"))
    # to file
    f = open("test.xml", "w+")
    f.write(doc.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8"))
    f.close