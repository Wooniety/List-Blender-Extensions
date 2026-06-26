import bpy
import addon_utils
from datetime import datetime

class LISTBLENDEREXTENSIONS_Utilities:
	def __init__(self):
		self.addons = []
		self.addonsFile = ""

		self.file = ""
		self.filetype = ""
		self.filename = ""

		self.toggleAuthor = True
		self.toggleExtensionDesc = True
		self.toggleExtensionVer = True
		self.toggleBlenderVer = True
		self.toggleWebsite = True
		self.toggleCategory = True

	def getFiletype(self):
		return self.filetype

	def setFiletype(self, filetype):
		self.filetype = filetype
		return self.filetype
	
	def setFilename(self, filename="", filetype=""):
		if filename == "":
			filename = "extensionList_" + datetime.now().strftime("%d-%m-%Y_%H-%M")
		
		if filetype == "":
			filetype = self.filetype
		
		self.filename = filename + "." + filetype
		return self.filename

	def getFilename(self):
		return self.filename

	def setToggleAuthor(self, value:bool):
		self.toggleAuthor = value
		return self.toggleAuthor

	def setToggleExtensionDesc(self, value:bool):
		self.toggleExtensionDesc = value
		return self.toggleExtensionDesc

	def setToggleExtensionVer(self, value:bool):
		self.toggleExtensionVer = value
		return self.toggleExtensionVer

	def setToggleBlenderVer(self, value:bool):
		self.toggleBlenderVer = value
		return self.toggleBlenderVer

	def setToggleWebsite(self, value:bool):
		self.toggleWebsite = value
		return self.toggleWebsite

	def setToggleCategory(self, value:bool):
		self.toggleCategory = value
		return self.toggleCategory

	def loadListOfAddons(self):
		self.addons = []
		for addon in addon_utils.modules():
			# default items
			filtered_details = {
				"Name": addon["name"]
			}

			if self.toggleAuthor:
				filtered_details['Author'] = addon['author']
			
			if self.toggleCategory:
				filtered_details['Category'] = addon['category']
			
			if self.toggleExtensionDesc:
				filtered_details['Description'] = addon['description']

			if self.toggleExtensionVer:
				filtered_details['Version'] = ".".join(addon['version'])

			if self.toggleBlenderVer:
				filtered_details['Blender Version'] = ".".join(addon['blender'])

			if self.toggleExtensionDesc:
				filtered_details['Website'] = addon['doc_url']

			self.addons.append(filtered_details)
		return self.addons
		
	def printAddonList(self):
		print(type(self.addons[0]))
	
	def exportAddonListToCSV(self):
		self.setFiletype("csv")
		pass
	
	def exportAddonListToCSV(self):
		pass
	
	def exportAddonListToTXT(self):
		pass
	
	def saveFile(self):
		pass