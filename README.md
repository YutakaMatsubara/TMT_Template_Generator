# TMT-Template-Generator

## About
A Template generator for Threat Modeling Tool(TMT) 2016.
> Microsoft Threat Modeling Tool 2016 is a tool that helps in finding threats in the design phase of software projects.

For more information about TMT 2016, please refer to [What’s New with Microsoft Threat Modeling Tool 2016](https://blogs.microsoft.com/cybertrust/2015/10/07/whats-new-with-microsoft-threat-modeling-tool-2016/).
To download and install TMT 2016, please refer to [Microsoft Threat Modeling Tool 2016](https://www.microsoft.com/en-us/download/details.aspx?id=49168).

## How does this work
+ This software consists of 3 python scripts: main.py, ElementTree.py and xmlparsing.py.
+ main.py: Prepare all the needed arguments and call functions in the ElementTree.py to actually start creating the xml tree.
+ ElementTree.py: Functions for creating the xml tree.
+ xmlparsing.py: Read Threat information from a XML-formatted database file.

## Requirements
+ Python 3.0 or higher

## Input
No input is required at current development level.

## Output
A TMT formatted template ready to be imported into Threat Modeling Tool 2016.

## How to install
1. Clone or download the git project to your own local envirment.
`$ git clone https://github.com/essenciao7/TMT_Template_Generator.git`
2. Confirm that you have Python 3.0 or even higher installed in your environment.
`$ python --version`
3. Move the XML Database file to the project folder.
4. Open the main.py script, locate the statement of Threats = parse_xml("database.xml"). Change the database.xml to your database file name.
5. Python-run the main.py script to start generating the TMT template.
6. **Automation still under development. Coming out soon.** You should notice a test.xml file created inside the folder. Please rename the file to anyname you want but end with the filename extention of tb7. e.g. NewTemplate.tb7.
7. Launch the TMT 2016, then import the template, and start creating your security model and analyzing your model.