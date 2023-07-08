# pyRevit: script info
# ---
# script title: Set Rebar Solid and Unobscured In View
# script version: 1.0
# script authors: [Tu Nombre]
# script license: MIT

# import the necessary modules
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector
from Autodesk.Revit.UI.Selection import ObjectType
from pyrevit import revit, DB
from pyrevit import script

__author__ = '[Tu Nombre]'
__context__ = 'selection'

# get the active document and view
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
view = uidoc.ActiveView

# start a transaction
with revit.Transaction('Set Rebar Solid and Unobscured In View'):
    # collect all rebar elements
    rebars = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsNotElementType().ToElements()

    # iterate over each rebar element
    for rebar in rebars:
        # set the rebar as solid and unobscured in the view
        rebar.SetSolidInView(view, True)
        rebar.SetUnobscuredInView(view, True)

# show the result
script.show_output(rebars)