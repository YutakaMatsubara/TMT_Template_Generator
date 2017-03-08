# TMT-Template-Generator

## About
A Template auto generator for Microsoft® Threat Modeling Tool(TMT) 2016.
> Microsoft Threat Modeling Tool 2016 is a tool that helps in finding threats in the design phase of software projects.

For more information about TMT 2016, please refer to [What’s New with Microsoft Threat Modeling Tool 2016](https://blogs.microsoft.com/cybertrust/2015/10/07/whats-new-with-microsoft-threat-modeling-tool-2016/).
To download and install TMT 2016, please refer to [Microsoft Threat Modeling Tool 2016](https://www.microsoft.com/en-us/download/details.aspx?id=49168).

## How does this work
+ This software consists of 3 python scripts: main.py, ElementTree.py and xmlparsing.py.
+ main.py: Prepare all the needed arguments and call functions in the ElementTree.py to actually start creating the xml tree.
+ ElementTree.py: Functions for creating the xml tree.
+ xmlparsing.py: Parsing the given XML-formatted database file to read stencils data as well as threat information data. And main.py will use the data in order to create the XML tree.

## Requirements
+ Python 3.0 or higher
+ Microsoft® Threat Modeling Tool 2016

## Input
+ A XML-formatted database file containing datas about stencils information. And the following fields are required for each record.
  + GenericElementName, for the stencil's name.
  + GenericElementHidden, for setting whether to hide the element or not when threat-model the system with TMT 2016. Boolean value: true or false.
  + GenericElementRepresentation, for describing the shape of current element when threat-model the system with TMT 2016. A "Rectangle" for target stencils, and a "Line" for flow stencils.
  + GenericeElementStrokeThickness, generally set as 0.
+ A XML-formatted database file containing datas about threat information.
  + ThreatCategoryName, for guidewords.
  + ThreatCategoryShortDescription, for a short description of the guideword.
  + ThreatTypeShortTitle, for a short title of effects when applying the current guideword to system.
  + ThreatTypeDescription, for a full version of effects when applying the current guideword to system.
  Noted that {source.Name}, {target.Name} and {flow.Name} within the description will be replaced by the real element within the threat model by TMT 2016.
  + ThreatTypePriority, for setting a priority of the current threat or risk.
+ A filename for saving the newly generated template file.

A practical way to prepare the database files is to use spreadsheet software such as Excel, and save the file with XML extension. In this git repository, there are also sample databases for both stencils and threats, refer to the 2 XML files for more info.
## Output
A TMT formatted template ready to be imported into Microsoft® Threat Modeling Tool 2016.

## How to install
1. Clone or download the git project to your own local environment.
~~~~
$ git clone https://github.com/essenciao7/TMT_Template_Generator.git
~~~~
2. Confirm that you have Python 3.0 or even higher installed in your environment by using the command below.
~~~~
$ python --version
~~~~
3. Move the XML Database file to the project folder.
4. Python-run the main.py script, and the prompt will ask you for the following inputs, after which the process should begin.
    * A filename for stencil database is required.
    * A filename for threat information database is required.
    * A filename for saving the newly generated template is required.
5. You should notice that a new file with an extention of tb7 will be generated in the designated location. e.g. NewTemplate.tb7.
6. Launch the TMT 2016, then import the template, and start creating your security model and analyzing your model.
