import bpy
import addon_utils
import csv, io, json
from datetime import datetime

class LISTBLENDEREXTENSIONS_Utilities:
	def __init__(self):
		self.addons = []
		self.addonsFile = ""

		self.filename = ""
		self.filetype = ""
		self.filecontents = ""

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
		for module in addon_utils.modules():
			info = addon_utils.module_bl_info(module)
			if info is None:
				continue

			filtered_details = {
				"Name": info.get("name", "")
			}

			if self.toggleAuthor:
				filtered_details['Author'] = info.get('author', "")
			if self.toggleCategory:
				filtered_details['Category'] = info.get('category', "")
			if self.toggleExtensionDesc:
				filtered_details['Description'] = info.get('description', "")
			if self.toggleExtensionVer:
				version = info.get('version', ())
				filtered_details['Version'] = ".".join(str(v) for v in version)
			if self.toggleBlenderVer:
				blender = info.get('blender', ())
				filtered_details['Blender Version'] = ".".join(str(v) for v in blender)
			if self.toggleWebsite:
				filtered_details['Website'] = info.get('doc_url', "")

			self.addons.append(filtered_details)
		return self.addons

	def printAddonList(self):
		print(type(self.addons[0]))
	
	def getFileContents(self, filetype:str):
		return self.filecontents

	def exportAddonListToCSV(self):
		# if empty
		if len(self.addons)==0:
			self.filecontents = ""
			return self.filecontents

		fieldnames = list(self.addons[0].keys())
		output = io.StringIO()

		# csv writing
		writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
		writer.writeheader()
		writer.writerows(self.addons)

		self.filecontents = output.getvalue()
		return self.filecontents

	def exportAddonListToTXT(self):
		lines = []
		for addon in self.addons:
			lines.append(addon.get("Name", ""))
			for key, value in addon.items():
				if key == "Name":
					continue
				lines.append(f"    {key}: {value}")
			lines.append("")
		self.filecontents = "\n".join(lines)
		return self.filecontents

	def exportAddonListToJSON(self):
		self.filecontents = json.dumps(self.addons, indent=2)
		return self.filecontents

	def getFileContents(self, filetype:str):
		if filetype == "csv":
			return self.exportAddonListToCSV()
		elif filetype == "txt":
			return self.exportAddonListToTXT()
		elif filetype == "json":
			return self.exportAddonListToJSON()
		return ""