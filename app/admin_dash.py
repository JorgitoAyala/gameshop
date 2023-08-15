# importing files
from utils.console import drawUI, drawTables, clear, lazyMessage
from api.general import searchByAttribute, getQuantity, addData
from utils.security import encrypt
from utils.validation import validationInfo
from utils.conversion import lineStringWrap

# Dashboard del administrador OPCION 1: Gestionar productos (juegos)
def manageProducts(type_of_user: str, user_id: str):
  clear()

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Gestionar productos 🤓 "))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Que deseas hacer? 🤔"))
  print(drawUI(1, ""))
  print(drawUI(3, "A) Ver todos los juegos 🎮"))
  print(drawUI(3, "B) Agregar un juego nuevo 😄"))
  print(drawUI(3, "C) Editar un juego existente 😄"))
  print(drawUI(3, "D) Eliminar un juego existente 👾"))
  print(drawUI(3, "E) Volver al dashboard principal 😮"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": viewAllProducts()
    case "B": print()
    case "C": print()
    case "D": print()
    case "E":
      from app.dashboard import userDashboard
      return userDashboard(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return manageProducts(type_of_user, user_id)


def viewAllProducts():
  clear()

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Juegos de Gameshop 🤓 !! "))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  print("*"*40 + "  " + "*"*40)
  print(drawTables(1, {"p1": "", "p2": ""}))
  print(drawTables(1, {"p1": " Juego del ahorcado ", "p2": " Hey! Adivina el número "}))
  print(drawTables(1, {"p1": "", "p2": ""}))
  print(drawTables(3, {"p1": "Hecho en: Python 🐍", "p2": "Hecho en: Pseint 🤠"}))
  print(drawTables(1, {"p1": "", "p2": ""}))
  print(drawTables(2, {"p1": "Id: P3", "p2": "Id: P4"}))
  print(drawTables(2, {"p1": "Categoría: puzzles", "p2": "Categoría: mente"}))
  print(drawTables(2, {"p1": "Precio: S/. 12.00", "p2": "Precio: S/. 10.00"}))
  print(drawTables(2, {"p1": "Objetivo: rescata al ahorcado!", "p2": "Objetivo: Prueba tu suerte!"}))
  print(drawTables(2, {"p1": "Cantidad comprada: 18", "10": "Cantidad comprada: 15"}))
  print(drawTables(1, {"p1": "", "p2": ""}))
  print("*"*40 + "  " + "*"*40)
  print()


def createProduct():
  print()

def updateProduct(product_id: str):
  print()

def deleteProduct(product_id: str):
  print()


# Dashboard del administrador OPCION 2: Gestionar clientes
def manageClients(type_of_user: str, user_id: str):
  clear()

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Gestionar clientes 🧑‍🤝‍🧑 "))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Que deseas hacer? 🤓🤔"))
  print(drawUI(1, ""))
  print(drawUI(3, "A) Ver todos los clientes 🎮"))
  print(drawUI(3, "B) Agregar a un cliente nuevo 😄"))
  print(drawUI(3, "C) Editar la información de un cliente existente 🎮"))
  print(drawUI(3, "D) Eliminar a un cliente existente 👾"))
  print(drawUI(3, "E) Volver al dashboard principal 😮"))
  print(drawUI(1, ""))
  print("*"*82)

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": print()
    case "B": print()
    case "C": print()
    case "D": print()
    case "E":
      from app.dashboard import userDashboard
      return userDashboard(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return manageProducts(type_of_user, user_id)

# Si quiero eliminar un cliente debo actualizar el id de todos los registros en orden