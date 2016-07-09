# TMT-Template-Generator

## About
A Template generator for Threat Modeling Tool(TFT) 2016.
> Microsoft Threat Modeling Tool 2016 is a tool that helps in finding threats in the design phase of software projects.

For more information about TFT 2016, please refer to [What’s New with Microsoft Threat Modeling Tool 2016](https://blogs.microsoft.com/cybertrust/2015/10/07/whats-new-with-microsoft-threat-modeling-tool-2016/).
To download and install TFT 2016, please refer to [Microsoft Threat Modeling Tool 2016](https://www.microsoft.com/en-us/download/details.aspx?id=49168).

## How does this work
+ This software consists of two python scripts: main.py and ElementTree.py.
+ main.py: Prepare all the needed arguments and call functions in the ElementTree.py to actually start creating the xml tree.
+ ElementTree.py: Functions for creating the xml tree.

## Requirements
+ Python 3.0 or higher

## Input
No input is required at current development level.

## Output
A TFT formatted template ready to be imported into Threat Modeling Tool 2016.

## How to install
1. Clone or download the git project to your own local envirment.
`$ git clone https://github.com/essenciao7/TMT_Template_Generator.git`
2. Confirm that you have Python 3.0 or even higher installed in your environment.
`$ python --version`
3. Python-run the main.py script to start generating the TFT template.
4. *Automation still under development. Coming out soon.*You should notice a test.xml file created inside the folder. Please rename the file to anyname you want but end with the filename extention of tb7. e.g. NewTemplate.tb7.
5. Launch the TFT 2016, then import the template, and startcreating your security model and analyzing your model.