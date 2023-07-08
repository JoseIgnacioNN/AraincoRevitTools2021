# pyRevit: script info
# ---
# script title: Set Rebar Solid and Unobscured In View
# script version: 1.0
# script authors: [Tu Nombre]
# script license: MIT

# Importar las referencias necesarias
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector, Transaction

# Obtener los servicios de Revit
doc = __revit__.ActiveUIDocument.Document
uiapp = __revit__.Application
uidoc = __revit__.ActiveUIDocument

# Recopilar los elementos de refuerzo
rebars = [rebar for rebar in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsNotElementType()]

# Obtener la vista activa
view = doc.ActiveView

# Iniciar la transacción
transaction = Transaction(doc, "Set Rebar Solid and Unobscured In View")
transaction.Start()

try:
    # Establecer los elementos de refuerzo como sólidos y no ocultos en la vista activa
    for rebar in rebars:
        rebar.SetSolidInView(view, True)
        rebar.SetUnobscuredInView(view, True)

    # Confirmar la transacción
    transaction.Commit()
except:
    # Anular la transacción en caso de errores
    transaction.RollBack()
    raise

# Imprimir los elementos de refuerzo
OUT = rebars


