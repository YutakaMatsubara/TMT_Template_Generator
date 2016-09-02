import xml.dom.minidom
import sys
import uuid

Threats = []
Stencils = []

class Threat:

	# TC for ThreatCategory, TT for ThreatType
	def create_Threat(self, attribute_no, attribute):
		if attribute_no == 1:
			self.TCName = attribute
		elif attribute_no == 3:
			self.TCShortDescription = attribute
		elif attribute_no == 5:
			self.TTShortTitle = attribute
		elif attribute_no == 7:
			self.TTDescription = attribute
		elif attribute_no == 9:
			self.TTPriority = attribute

	def showThreat(self):
		print("===== %s =====" % self.TCName)
		print(self.TCName)
		print(self.TCShortDescription)
		print(self.TTShortTitle)
		print(self.TTDescription)
		print(self.TTPriority)
		print("===== %s =====" % self.TCName)

class Stencil:
	
	def create_Stencil(self, attribute_no, attribute):
		if attribute_no == 1:
			self.GEName = attribute
		elif attribute_no == 3:
			self.GERepresentation = attribute


	def showStencil(self):
		print("===== %s =====" % self.GEName)
		print(self.GEName)
		print(self.GERepresentation)
		print("===== %s =====" % self.GEName)

def parse_xml(db):
	# use the parse() funciton to load and parse an XML file
	try:
		if(not db.endswith(".xml")):
			raise ValueError("File name must end with .xml.")
		doc = xml.dom.minidom.parse(db)
	except FileNotFoundError as e:
		print("Abort: Could not open the file.", e)
		sys.exit()
	except ValueError as e:
		print("Abort: Bad file name.", e)
		sys.exit()

	print(doc.nodeName)
	print(doc.firstChild.tagName)

	Rows = doc.getElementsByTagName("Row")
	row_counter = 0
	threat_counter = 0
	print("%d Rows:" % Rows.length)
	for (i, Row) in enumerate(Rows):
		# ignore the header title cells
		if i == 0:
			continue

		Threats.insert(threat_counter, Threat())
		for (j, Cell) in enumerate(Row.childNodes):
			# print(Cell.firstChild.nodeValue)
			for Data in Cell.childNodes:
				# print(Data.firstChild.nodeValue)
				# print("Setting %d." % j)
				Threats[threat_counter].create_Threat(j, Data.firstChild.nodeValue)
		Threats[threat_counter].showThreat()
		threat_counter = threat_counter + 1

	return Threats

def parse_xml2(db):
	# use the parse() funciton to load and parse an XML file.
	try:
		if(not db.endswith(".xml")):
			raise ValueError("File name must end with .xml.")
		doc = xml.dom.minidom.parse(db)
	except FileNotFoundError as e:
		print("Abort: Could not open the file.", e)
		sys.exit()
	except ValueError as e:
		print("Abort: Bad file name.", e)
		sys.exit()

	print(doc.nodeName)
	print(doc.firstChild.tagName)

	Rows = doc.getElementsByTagName("Row")
	row_counter = 0
	stencil_counter = 0
	print("%d Rows:" % Rows.length)
	for (i, Row) in enumerate(Rows):
		# ignore the header title cells
		if i == 0:
			continue

		Stencils.insert(stencil_counter, Stencil())
		for (j, Cell) in enumerate(Row.childNodes):
			# print(Cell.firstChild.nodeValue)
			for Data in Cell.childNodes:
				# print(Data.firstChild.nodeValue)
				# print("Setting %d." % j)
				Stencils[stencil_counter].create_Stencil(j, Data.firstChild.nodeValue)
		Stencils[stencil_counter].showStencil()
		stencil_counter = stencil_counter + 1

	return Stencils
