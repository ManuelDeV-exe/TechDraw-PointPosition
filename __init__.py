import FreeCAD
import FreeCADGui
import TechDraw
import os

class Meins:
    def GetResources(self):
        mypath = os.path.dirname(__file__)
        return {
             'Pixmap': mypath + "/Icons/QuickMeasure.svg",
             'MenuText': 'test Measure',
             'ToolTip': 'test'
             }

    def Activated(self, placeholder = None):
        print('Activated')

    def Deactivated(self):
        print('Deactivated')

    def IsEnabled(self):
        print('IsEnabled')
        return()

    def IsActive(self):
        print('IsActive')
        return(True)
    
FreeCADGui.addCommand('TechDrawWorkbench', Meins())
