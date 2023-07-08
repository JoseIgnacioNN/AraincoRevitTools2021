# pyRevit: script info
# ---
# script title: Set Rebar Solid and Unobscured In View
# script version: 1.0
# script authors: [Tu Nombre]
# script license: MIT

# Importar los módulos necesarios
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector

# Obtener el documento activo y la vista activa
doc = __revit__.ActiveUIDocument.Document
view = __revit__.ActiveUIDocument.ActiveView

# Iniciar una transacción
TransactionManager.Instance.EnsureInTransaction(doc)

# Recopilar todos los elementos de refuerzo
rebars = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsNotElementType().ToElements()

# Iterar sobre cada elemento de refuerzo
for rebar in rebars:
    # Establecer el elemento de refuerzo como sólido y no oculto en la vista activa
    rebar.SetSolidInView(view, True)
    rebar.SetUnobscuredInView(view, True)

# Confirmar la transacción
TransactionManager.Instance.TransactionTaskDone()

# Imprimir los elementos de refuerzo afectados
for rebar in rebars:
    print(rebar.Id)

