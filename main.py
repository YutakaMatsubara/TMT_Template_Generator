import xml.dom.minidom
import uuid

from ElementTree import *

t_name = "Service Level"
t_id = str(uuid.uuid4())
t_version = "1.0.0.2"
t_author = "TMT Template Generator"

def main():
    KnowledgeBase_node = KnowledgeBase(t_name, t_version, t_author)
    # KnowledgeBase = create_KnowledgeBase(t_name, t_id, t_version, t_author)
    root = KnowledgeBase_node.create_KnowledgeBase()
    doc.appendChild(root)

    if root.hasChildNodes():
        for node in root.childNodes:
            if node.nodeName == "ThreatMetaData":
                Title = PropertiesMetaData("Title", "Title", "false", "", "0")
                Title.create_Values("Not Set")

                UserThreatCategory = PropertiesMetaData("UserThreatCategory", "Category", "false", "", "0")
                UserThreatCategory.create_Values("")

                UserThreatShortDescription = PropertiesMetaData("UserThreatShortDescription", "Short Description", "false", "", "0")
                UserThreatShortDescription.create_Values("Not Set")

                UserThreatDescription = PropertiesMetaData("UserThreatDescription", "Description", "false", "", "0")
                UserThreatDescription.create_Values("Not Set")

                StateInformation = PropertiesMetaData("StateInformation", "Justification", "false", "", "0")
                StateInformation.create_Values("Not Set")

                InteractionString = PropertiesMetaData("InteractionString", "Interaction", "false", "", "0")
                InteractionString.create_Values("Not Set")

                Priority = PropertiesMetaData("Priority", "Priority", "false", "Priority", "1")
                Priority.create_Values("High", "Medium", "Low")

                PropertiesMetaData_node = create_PropertiesMetaData(Title.create_ThreatMetaDatum(), UserThreatCategory.create_ThreatMetaDatum(), UserThreatShortDescription.create_ThreatMetaDatum(), UserThreatDescription.create_ThreatMetaDatum(), StateInformation.create_ThreatMetaDatum(), InteractionString.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                ThreatMetaData_new = create_ThreatMetaData("true", "true", PropertiesMetaData_node)
                root.replaceChild(ThreatMetaData_new, node)
                continue

            elif node.nodeName == "GenericElements":
                Automobiles = GenericElement("Automobiles", "", "ROOT", "", "false", "Rectangle", "0", "", "")
                node.appendChild(Automobiles.create_ElementType())

                KeyFob = GenericElement("Key Fob", "", "ROOT", "", "false", "Rectangle", "0", "", "")
                node.appendChild(KeyFob.create_ElementType())

                KeyFobAuth = GenericElement("Key fob authorization within the communication range", "", "ROOT", "", "false", "Line", "0", "", "")
                node.appendChild(KeyFobAuth.create_ElementType())

                GenericOperationalRequest = GenericElement("Generic Operational Request", "", "ROOT", "", "false", "Line", "0", "", "")
                node.appendChild(GenericOperationalRequest.create_ElementType())

                FreeTextAnnotation = GenericElement("Free Text Annotation", "A representation of an annotation.", "ROOT", "", "true", "Annotation", "0", "", "")
                node.appendChild(FreeTextAnnotation.create_ElementType())

            elif node.nodeName == "StandardElements":
                UnlockingTheDoor = StandardElement("Unlocking the door", "", GenericOperationalRequest.id, "", "", "false", "Line", "0", "", "")
                node.appendChild(UnlockingTheDoor.create_ElementType())

                OpeningTheTrunk = StandardElement("Opening the trunk", "", GenericOperationalRequest.id, "", "", "false", "Line", "0", "", "")
                node.appendChild(OpeningTheTrunk.create_ElementType())

                LockingTheDoor = StandardElement("Locking the door", "", GenericOperationalRequest.id, "", "", "false", "Line", "0", "", "")
                node.appendChild(LockingTheDoor.create_ElementType())

            elif node.nodeName == "ThreatCategories":
                Omission = ThreatCategory("Omission", "The service is never deliverd.")
                node.appendChild(Omission.create_ThreatCategory())

                Commision = ThreatCategory("Commision", "A service is delivered when not required.")
                node.appendChild(Commision.create_ThreatCategory())

                Early = ThreatCategory("Early", "The service (communication) occurs earlier than intended.")
                node.appendChild(Early.create_ThreatCategory())

                Late = ThreatCategory("Late", "The Service (communication) occurs later than intended.")
                node.appendChild(Late.create_ThreatCategory())

                Value = ThreatCategory("Value", "The information (data) delivered has the wrong value.")
                node.appendChild(Value.create_ThreatCategory())

            elif node.nodeName == "ThreatTypes":
                ThreatType_Omission = ThreatType("Service Omitted", Omission.id, "", "{flow.Name} will not be initiated between {source.Name} and {target.Name}.")
                ThreatType_Omission.create_IEStatement(Automobiles.id, KeyFob.id)
                UserThreatDescription.create_Values("{flow.Name} will not be initiated between {source.Name} and {target.Name}.")
                Priority.create_Values("High")
                PropertiesMetaData_node = create_PropertiesMetaData(UserThreatDescription.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                node.appendChild(ThreatType_Omission.create_ThreatType(PropertiesMetaData_node))

                ThreatType_Commision = ThreatType("Unproper Service Commision", Commision.id, "", "{flow.Name} will be commited, regardless of user's intention.")
                ThreatType_Commision.create_IEStatement(Automobiles.id, KeyFob.id)
                UserThreatDescription.create_Values("{flow.Name} will be commited, regardless of user's intention.")
                Priority.create_Values("High")
                PropertiesMetaData_node = create_PropertiesMetaData(UserThreatDescription.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                node.appendChild(ThreatType_Commision.create_ThreatType(PropertiesMetaData_node))

                ThreatType_Early = ThreatType("Early Commited Service", Early.id, "", "It takes shorter than usual for service of {flow.Name} between {source.Name} and {target.Name}")
                ThreatType_Early.create_IEStatement(Automobiles.id, KeyFob.id)
                UserThreatDescription.create_Values("It takes shorter than usual for service of {flow.Name} between {source.Name} and {target.Name}")
                Priority.create_Values("Low")
                PropertiesMetaData_node = create_PropertiesMetaData(UserThreatDescription.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                node.appendChild(ThreatType_Early.create_ThreatType(PropertiesMetaData_node))

                ThreatType_Late = ThreatType("Unproper Service Commision", Late.id, "", "It takes longer than usual to commit the service of {flow.Name} between {source.Name} and {target.Name}.")
                ThreatType_Late.create_IEStatement(Automobiles.id, KeyFob.id)
                UserThreatDescription.create_Values("It takes longer than usual to commit the service of {flow.Name} between {source.Name} and {target.Name}.")
                Priority.create_Values("Medium")
                PropertiesMetaData_node = create_PropertiesMetaData(UserThreatDescription.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                node.appendChild(ThreatType_Late.create_ThreatType(PropertiesMetaData_node))

                ThreatType_Value = ThreatType("Unproper Service Commision", Value.id, "", "A completely different service rather than {flow.Name} between {source.Name} and {target.Name} will be commited.")
                ThreatType_Value.create_IEStatement(Automobiles.id, KeyFob.id)
                UserThreatDescription.create_Values("A completely different service rather than {flow.Name} between {source.Name} and {target.Name} will be commited.")
                Priority.create_Values("High")
                PropertiesMetaData_node = create_PropertiesMetaData(UserThreatDescription.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                node.appendChild(ThreatType_Value.create_ThreatType(PropertiesMetaData_node))

# Output the XML file to disk.
    create_xml_file()

if __name__ == "__main__":
    main();