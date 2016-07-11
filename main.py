import xml.dom.minidom
import uuid

from ElementTree import *

whitespace = " "

t_name = "Service Level"
t_id = str(uuid.uuid4())
t_version = "1.0.0.2"
t_author = "TMT Template Generator"

Title_uuid = str(uuid.uuid4())
UserThreatCategory_uuid = str(uuid.uuid4())
UserThreatShortDescription_uuid = str(uuid.uuid4())
UserThreatDescription_uuid = str(uuid.uuid4())
StateInformation_uuid = str(uuid.uuid4())
InteractionString_uuid = str(uuid.uuid4())
Priority_uuid = str(uuid.uuid4())

Automobiles_uuid = str(uuid.uuid4())
KeyFob_uuid = str(uuid.uuid4())

Omission_uuid = str(uuid.uuid4())

def main():
    KnowledgeBase = create_KnowledgeBase(t_name, t_id, t_version, t_author)
    doc.appendChild(KnowledgeBase)

    if KnowledgeBase.hasChildNodes():
        for node in KnowledgeBase.childNodes:
            if node.nodeName == "ThreatMetaData":
                Title_Values = create_Values("Not Set")
                Title = PropertiesMetaData("Title", "Title", "false", Title_Values, "", "0")

                UserThreatCategory_Values = create_Values("")
                UserThreatCategory = PropertiesMetaData("UserThreatCategory", "Category", "false", UserThreatCategory_Values, "", "0")

                UserThreatShortDescription_Values = create_Values("Not Set")
                UserThreatShortDescription = PropertiesMetaData("UserThreatShortDescription", "Short Description", "false", UserThreatShortDescription_Values, "", "0")

                UserThreatDescription_Values = create_Values("Not Set")
                UserThreatDescription = PropertiesMetaData("UserThreatDescription", "Description", "false", UserThreatDescription_Values, "", "0")

                StateInformation_Values = create_Values("Not Set")
                StateInformation = PropertiesMetaData("StateInformation", "Justification", "false", StateInformation_Values, "", "0")

                InteractionString_Values = create_Values("Not Set")
                InteractionString = PropertiesMetaData("InteractionString", "Interaction", "false", InteractionString_Values, "", "0")

                Priority_Values = create_Values("High", "Medium", "Low")
                Priority = PropertiesMetaData("Priority", "Priority", "false", Priority_Values, "Priority", "1")

                PropertiesMetaData_node = create_PropertiesMetaData(Title.create_ThreatMetaDatum(), UserThreatCategory.create_ThreatMetaDatum(), UserThreatShortDescription.create_ThreatMetaDatum(), UserThreatDescription.create_ThreatMetaDatum(), StateInformation.create_ThreatMetaDatum(), InteractionString.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                ThreatMetaData_new = create_ThreatMetaData("true", "true", PropertiesMetaData_node)
                KnowledgeBase.replaceChild(ThreatMetaData_new, node)
                continue
                # ThreatMetaData = create_ThreatMetaData()
                # node.appendChild(ThreatMetaData)
                # for node in ThreatMetaData.childNodes:
                #     if node.nodeName == "PropertiesMetaData":
                #         Title_Values = create_Values("Not Set")
                #         Title = create_ThreatMetaDatum("Title", "Title", "false", Title_Values, "", str(uuid.uuid4()), "0")
                #         node.appendChild(Title)

                #         UserThreatCategory_Values = create_Values("")
                #         UserThreatCategory = create_ThreatMetaDatum("UserThreatCategory", "Category", "false", UserThreatCategory_Values, "", "", "0")
                #         node.appendChild(UserThreatCategory)

                #         UserThreatShortDescription_Values = create_Values("Not Set")
                #         UserThreatShortDescription = create_ThreatMetaDatum("UserThreatShortDescription", "Short Description", "false", UserThreatShortDescription_Values, "", str(uuid.uuid4()), "0")
                #         node.appendChild(UserThreatShortDescription)

                #         UserThreatDescription_Values = create_Values("Not Set")
                #         UserThreatDescription = create_ThreatMetaDatum("UserThreatDescription", "Description", "false", UserThreatDescription_Values, "", str(uuid.uuid4()), "0")
                #         node.appendChild(UserThreatDescription)

                #         StateInformation_Values = create_Values("Not Set")
                #         StateInformation = create_ThreatMetaDatum("StateInformation", "Justification", "false", StateInformation_Values, "", str(uuid.uuid4()), "0")
                #         node.appendChild(StateInformation)

                #         InteractionString_Values = create_Values("Not Set")
                #         InteractionString = create_ThreatMetaDatum("InteractionString", "Interaction", "false", InteractionString_Values, "", str(uuid.uuid4()), "0")
                #         node.appendChild(InteractionString)

                #         Priority_Values = create_Values("High", "Medium", "Low")
                #         Priority = create_ThreatMetaDatum("Priority", "Priority", "false", Priority_Values, "Priority", str(uuid.uuid4()), "1")
                #         node.appendChild(Priority)
            elif node.nodeName == "GenericElements":
                Automobiles = GenericElement("Automobiles", "", "ROOT", "", "false", "Rectangle", "0", "", "")
                node.appendChild(Automobiles.create_ElementType())

                KeyFob = GenericElement("Key Fob", "", "ROOT", "", "false", "Rectangle", "0", "", "")
                node.appendChild(KeyFob.create_ElementType())

                GenericOperationalRequest = GenericElement("Generic Operational Request", "", "ROOT", "", "false", "Line", "0", "", "")
                node.appendChild(GenericOperationalRequest.create_ElementType())

            elif node.nodeName == "StandardElements":
                UnlockingTheDoor = StandardElement("Unlocking the door", "", GenericOperationalRequest.id, "", "", "false", "Line", "0", "", "")
                node.appendChild(UnlockingTheDoor.create_ElementType())
            elif node.nodeName == "ThreatCategories":
                Omission = ThreatCategory("Omission", "The service is never deliverd.")
                node.appendChild(Omission.create_ThreatCategory())

            elif node.nodeName == "ThreatTypes":
                Include1 = create_IncludeStatement(Automobiles_uuid, KeyFob_uuid)
                GenerationFilters1 = create_GenerationFilters(Include1, "")

                UserThreatDescription.changeValues("{flow.Name} will not be initiated between {source.Name} and {target.Name}.")
                PropertiesMetaData_node = create_PropertiesMetaData(UserThreatDescription.create_ThreatMetaDatum(), Priority.create_ThreatMetaDatum())
                ThreatType = create_ThreatType(GenerationFilters1, str(uuid.uuid4()), "Service Omitted", Omission_uuid, "", "{flow.Name} will not be initiated between {source.Name} and {target.Name}.", PropertiesMetaData_node)
                node.appendChild(ThreatType)


# Output the XML file to disk.
    create_xml_file()

if __name__ == "__main__":
    main();