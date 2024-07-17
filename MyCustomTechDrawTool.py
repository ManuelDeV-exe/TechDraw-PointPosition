import FreeCAD
import FreeCADGui
import TechDraw

class MyCustomTechDrawTool:
    def Activated(self):
        FreeCAD.Console.PrintMessage("Mein TechDraw-Tool wurde aktiviert!\n")
        # Hier fügen Sie Ihre benutzerdefinierten TechDraw-Funktionen hinzu
       
    def IsActive(self):
        return True

FreeCADGui.addCommand('MyCustomTechDrawTool', MyCustomTechDrawTool())
