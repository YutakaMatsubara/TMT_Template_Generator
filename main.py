import xml.dom.minidom
import uuid

from ElementTree import *

whitespace = " "

t_name = "Service Level"
t_id = str(uuid.uuid4())
t_version = "1.0.0.2"
t_author = "TMT Template Generator"

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
                Title = create_ThreatMetaDatum("Title", "Title", "false", Title_Values, "", str(uuid.uuid4()), "0")

                UserThreatCategory_Values = create_Values("")
                UserThreatCategory = create_ThreatMetaDatum("UserThreatCategory", "Category", "false", UserThreatCategory_Values, "", "", "0")

                UserThreatShortDescription_Values = create_Values("Not Set")
                UserThreatShortDescription = create_ThreatMetaDatum("UserThreatShortDescription", "Short Description", "false", UserThreatShortDescription_Values, "", str(uuid.uuid4()), "0")

                UserThreatDescription_Values = create_Values("Not Set")
                UserThreatDescription = create_ThreatMetaDatum("UserThreatDescription", "Description", "false", UserThreatDescription_Values, "", str(uuid.uuid4()), "0")

                StateInformation_Values = create_Values("Not Set")
                StateInformation = create_ThreatMetaDatum("StateInformation", "Justification", "false", StateInformation_Values, "", str(uuid.uuid4()), "0")

                InteractionString_Values = create_Values("Not Set")
                InteractionString = create_ThreatMetaDatum("InteractionString", "Interaction", "false", InteractionString_Values, "", str(uuid.uuid4()), "0")

                Priority_Values = create_Values("High", "Medium", "Low")
                Priority = create_ThreatMetaDatum("Priority", "Priority", "false", Priority_Values, "Priority", str(uuid.uuid4()), "1")

                PropertiesMetaData = create_PropertiesMetaData(Title, UserThreatCategory, UserThreatDescription, StateInformation, InteractionString, Priority)
                ThreatMetaData_new = create_ThreatMetaData("true", "true", PropertiesMetaData)
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
                Automobiles = create_GenericElementType("Automobiles", Automobiles_uuid, "", "ROOT", "", "false", "Rectangle", "0", "Centered on stencil", "")
                node.appendChild(Automobiles)

                KeyFob = create_GenericElementType("Key Fob", KeyFob_uuid, "", "ROOT", "", "false", "Rectangle", "0", "Centered on stencil", "")
                node.appendChild(KeyFob)
            elif node.nodeName == "StandardElements":
                StandardElementType = create_StandardElementType("Unlocking the door",  str(uuid.uuid4()), "", str(uuid.uuid4()), "", "", "false", "Line", "0", "", "")
                node.appendChild(StandardElementType)
            elif node.nodeName == "ThreatCategories":
                ThreatCategory = create_ThreatCategory("Omission", Omission_uuid, "The service is never deliverd.")
                node.appendChild(ThreatCategory)
            elif node.nodeName == "ThreatTypes":
                Include1 = create_IncludeStatement(Automobiles_uuid, KeyFob_uuid)
                GenerationFilters1 = create_GenerationFilters(Include1, "")

                UserThreatDescription_Values = create_Values("{flow.Name} will not be initiated between {source.Name} and {target.Name}.")
                UserThreatDescription = create_ThreatMetaDatum("UserThreatDescription", "Description", "false", UserThreatDescription_Values, "", str(uuid.uuid4()), "0")
                Priority_Values = create_Values("High", "Medium", "Low")
                Priority = create_ThreatMetaDatum("Priority", "Priority", "false", Priority_Values, "Priority", str(uuid.uuid4()), "1")
                PropertiesMetaData = create_PropertiesMetaData(UserThreatDescription, Priority)
                ThreatType = create_ThreatType(GenerationFilters1, str(uuid.uuid4()), "Service Omitted", Omission_uuid, "", "{flow.Name} will not be initiated between {source.Name} and {target.Name}.", PropertiesMetaData)
                node.appendChild(ThreatType)


# Output the XML file to disk.
    create_xml_file()

if __name__ == "__main__":
    main();