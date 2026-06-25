import bpy
import addon_utils

class ListBlenderExtensions:
    def __init__(self):
        self.addons = []
        self.filepath = self.setFileDirectory()
        self.addonsFile = ""

        self.toggleAuthor = False
        self.toggleVersionNum = True
        self.toggleCategory = False
        self.toggleWebsite = False
        self.toggleShowOnlyEnabled = True
    
    def setFileDirectory(self, filepath:str):
        # if empty set default to be somewhere
        pass

    def loadListOfAddons(self):
        self.addons = []
        for addon in addon_utils.modules():
            self.addons.append(addon_utils.module_bl_info(addon))
        
    def createAddonList(self):
        pass

    def printAddonList(self):
        print(self.addons)
    
    def exportAddonListToCSV(self):
        pass
    
    def exportAddonListToTXT(self):
        pass
    
    def saveFile(self):
        pass