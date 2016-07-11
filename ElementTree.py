'''
Created on Jun 3, 2016

@author: Jingxuan Wei
'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import Document
import uuid

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
class PropertiesMetaData:
    def __init__(self, name, label, hide_from_ui, values, description, attributes_type):
        self.name = name
        self.label = label
        self.hide_from_ui = hide_from_ui
        self.values = values
        self.description = description
        self.id = str(uuid.uuid4())
        self.attributes_type = attributes_type

    def create_ThreatMetaDatum(self):
        ThreatMetaDatum = doc.createElement("ThreatMetaDatum")

        ThreatMetaDatum_name = doc.createElement("Name")
        if self.name != "":
            ThreatMetaDatum_name.appendChild(doc.createTextNode(self.name))
        ThreatMetaDatum.appendChild(ThreatMetaDatum_name)

        ThreatMetaDatum_label = doc.createElement("Label")
        if self.label != "":
            ThreatMetaDatum_label.appendChild(doc.createTextNode(self.label))
        ThreatMetaDatum.appendChild(ThreatMetaDatum_label)        

        ThreatMetaDatum_hide_from_ui = doc.createElement("HideFromUI")
        if self.hide_from_ui != "":
            ThreatMetaDatum_hide_from_ui.appendChild(doc.createTextNode(self.hide_from_ui))
        ThreatMetaDatum.appendChild(ThreatMetaDatum_hide_from_ui)

        ThreatMetaDatum_values = doc.createElement("Values")
        if self.values != "":
            ThreatMetaDatum.appendChild(self.values)

        ThreatMetaDatum_description = doc.createElement("description")
        if self.description != "":
            ThreatMetaDatum_description.appendChild(doc.createTextNode(self.description))
        ThreatMetaDatum.appendChild(ThreatMetaDatum_description)  

        ThreatMetaDatum_id = doc.createElement("Id")
        ThreatMetaDatum_label.appendChild(doc.createTextNode(self.id))
        ThreatMetaDatum.appendChild(ThreatMetaDatum_id)  

        ThreatMetaDatum_attributes_type = doc.createElement("AttributeType")
        if self.attributes_type != "":
            ThreatMetaDatum_attributes_type.appendChild(doc.createTextNode(self.attributes_type))
        ThreatMetaDatum.appendChild(ThreatMetaDatum_attributes_type)          

        return ThreatMetaDatum

    def id(self):
        return self.id

    def changeValues(self, new_values):
        self.values = new_values

# create child element for ThreatMetaData: IsPriorityUsed, IsStatusUsed, PropertiesMetaData
# |KnowledgeBase
# |--ThreatMetaData
# |----IsPriorityUsed
# |----IsStatusUsed
# |----PropertiesMetaData
def create_ThreatMetaData(is_priority_used, is_status_used, properties_meta_data):
    ThreatMetaData_Children = ["IsPriorityUsed", "IsStatusUsed", "PropertiesMetaData"]
    ThreatMetaData = doc.createElement("ThreatMetaData")
    for child in ThreatMetaData_Children:
        if child == ThreatMetaData_Children[2]:
            ThreatMetaData.appendChild(properties_meta_data)
            continue
        else:
            ThreatMetaData_child = doc.createElement(child)
            ThreatMetaData.appendChild(ThreatMetaData_child)
            if child == ThreatMetaData_Children[0] and is_priority_used != "":
                ThreatMetaData_child.appendChild(doc.createTextNode(is_priority_used))
            elif child == ThreatMetaData_Children[1] and is_priority_used != "":
                ThreatMetaData_child.appendChild(doc.createTextNode(is_status_used))
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
class GenericElement:
    'Common base class for all Generic Elements'

    def __init__(self, name, description, parent_element, image, hidden, representation, stroke_thickness, image_location, attributes):

        self.name = name     
        self.id = str(uuid.uuid4())
        self.description = description
        self.parent_element = parent_element
        self.image = image
        self.hidden = hidden
        self.representation = representation
        self.stroke_thickness = stroke_thickness
        self.image_location = image_location
        self.attributes = attributes

    def create_ElementType(self):
        ElementType = doc.createElement("ElementType")

        ElementType_name = doc.createElement("Name")
        if self.name != "":
            ElementType_name.appendChild(doc.createTextNode(self.name))
        ElementType.appendChild(ElementType_name)
        
        ElementType_id = doc.createElement("ID")
        ElementType_id.appendChild(doc.createTextNode(self.id))
        ElementType.appendChild(ElementType_id)

        ElementType_parent_element = doc.createElement("ParentElement")
        if self.parent_element != "":
            ElementType_parent_element.appendChild(doc.createTextNode(self.parent_element))
        ElementType.appendChild(ElementType_parent_element)

        ElementType_image = doc.createElement("Image")
        if self.image != "":
            ElementType_image.appendChild(doc.createTextNode(self.image))
        ElementType.appendChild(ElementType_image)

        ElementType_hidden = doc.createElement("Hidden")
        if self.hidden != "":
            ElementType_hidden.appendChild(doc.createTextNode(self.hidden))
        ElementType.appendChild(ElementType_hidden)

        ElementType_representation = doc.createElement("Representation")
        if self.representation != "":
            ElementType_representation.appendChild(doc.createTextNode(self.representation))
        ElementType.appendChild(ElementType_representation)

        ElementType_stroke_thickness = doc.createElement("StrokeThickness")
        if self.stroke_thickness != "":
            ElementType_stroke_thickness.appendChild(doc.createTextNode(self.stroke_thickness))
        ElementType.appendChild(ElementType_stroke_thickness)

        ElementType_image_location = doc.createElement("ImageLocation")
        if self.image_location != "":
            ElementType_image_location.appendChild(doc.createTextNode(self.image_location))
        ElementType.appendChild(ElementType_image_location)

        ElementType_attributes = doc.createElement("Attributes")
        if self.attributes != "":
            ElementType_attributes.appendChild(doc.createTextNode(self.attributes))
        ElementType.appendChild(ElementType_attributes)

        return ElementType

    def id(self):
        return self.id

class StandardElement:
    'Common base class for all Standard Elements'

    def __init__(self, name, description, parent_element, image, image_stream, hidden, representation, stroke_thickness, image_location, attributes):
        self.name = name     
        self.id = str(uuid.uuid4())
        self.description = description
        self.parent_element = parent_element
        self.image = image
        self.image_stream = image_stream
        self.hidden = hidden
        self.representation = representation
        self.stroke_thickness = stroke_thickness
        self.image_location = image_location
        self.attributes = attributes

    def create_ElementType(self):
        ElementType = doc.createElement("ElementType")

        ElementType_name = doc.createElement("Name")
        if self.name != "":
            ElementType_name.appendChild(doc.createTextNode(self.name))
        ElementType.appendChild(ElementType_name)
        
        ElementType_id = doc.createElement("ID")
        ElementType_id.appendChild(doc.createTextNode(self.id))
        ElementType.appendChild(ElementType_id)

        ElementType_parent_element = doc.createElement("ParentElement")
        if self.parent_element != "":
            ElementType_parent_element.appendChild(doc.createTextNode(self.parent_element))
        ElementType.appendChild(ElementType_parent_element)

        ElementType_image = doc.createElement("Image")
        if self.image != "":
            ElementType_image.appendChild(doc.createTextNode(self.image))
        ElementType.appendChild(ElementType_image)

        ElementType_image_stream = doc.createElement("ImageStream")
        if self.image_stream != "":
            ElementType_image.appendChild(doc.createTextNode(self.image_stream))
        ElementType.appendChild(ElementType_image_stream)

        ElementType_hidden = doc.createElement("Hidden")
        if self.hidden != "":
            ElementType_hidden.appendChild(doc.createTextNode(self.hidden))
        ElementType.appendChild(ElementType_hidden)

        ElementType_representation = doc.createElement("Representation")
        if self.representation != "":
            ElementType_representation.appendChild(doc.createTextNode(self.representation))
        ElementType.appendChild(ElementType_representation)

        ElementType_stroke_thickness = doc.createElement("StrokeThickness")
        if self.stroke_thickness != "":
            ElementType_stroke_thickness.appendChild(doc.createTextNode(self.stroke_thickness))
        ElementType.appendChild(ElementType_stroke_thickness)

        ElementType_image_location = doc.createElement("ImageLocation")
        if self.image_location != "":
            ElementType_image_location.appendChild(doc.createTextNode(self.image_location))
        ElementType.appendChild(ElementType_image_location)

        ElementType_attributes = doc.createElement("Attributes")
        if self.attributes != "":
            ElementType_attributes.appendChild(doc.createTextNode(self.attributes))
        ElementType.appendChild(ElementType_attributes)

        return ElementType

    def id(self):
        return self.id

# create child element for ThreatCategory: "Name", "Id", "ShortDescription
# |ThreatCategory
# |--Name
# |--Id
# |--ShortDescription
class ThreatCategory:
    def __init__(self, name, short_description):
        self.name = name
        self.id = str(uuid.uuid4())
        self.short_description = short_description

    def create_ThreatCategory(self):
        ThreatCategory = doc.createElement("ThreatCategory")

        ThreatCategory_name = doc.createElement("Name")
        if self.name != "":
            ThreatCategory_name.appendChild(doc.createTextNode(self.name))
        ThreatCategory.appendChild(ThreatCategory_name)
        
        ThreatCategory_id = doc.createElement("Id")
        ThreatCategory_id.appendChild(doc.createTextNode(self.id))
        ThreatCategory.appendChild(ThreatCategory_id)

        ThreatCategory_short_description = doc.createElement("ShortDescription")
        if self.short_description != "":
            ThreatCategory_short_description.appendChild(doc.createTextNode(self.short_description))
        ThreatCategory.appendChild(ThreatCategory_short_description)

        return ThreatCategory

    def id(self):
        return self.id

class ThreatType:
    def __init__(self, generation_filters, short_title, category, related_category, description, properties_meta_data):
        self.generation_filters = generation_filters
        self.id = str(uuid.uuid4())
        self.short_title = short_title
        self.category = category
        self.related_category = related_category
        self.description = description
        self.properties_meta_data = properties_meta_data

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

def create_PropertiesMetaData(*ThreatMetaDatums):
    PropertiesMetaData = doc.createElement("PropertiesMetaData")
    for ThreatMetaDatum in ThreatMetaDatums:
        PropertiesMetaData.appendChild(ThreatMetaDatum)
    return PropertiesMetaData

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
        if child == ThreatType_Children[0]:
            ThreatType.appendChild(generation_filters)
            continue

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

        if child == ThreatType_Children[6]:
            ThreatType.appendChild(properties_meta_data)
            continue

    return ThreatType

# output xml documents to the console as well as to a file named: test.xml
def create_xml_file():
    # to console
    print (doc.toprettyxml(indent="  ", encoding="utf-8"))
    # to file
    f = open("test.xml", "w+")
    f.write(doc.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8"))
    f.close