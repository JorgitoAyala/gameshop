# importing files
from utils.console import drawUI, drawTables, clear, lazyMessage
from api.general import readAllData
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
    case "A": return viewAllProducts(type_of_user, user_id)
    case "B": return createProduct(type_of_user, user_id)
    case "C": return print()
    case "D": return print()
    case "E":
      from app.dashboard import userDashboard
      return userDashboard(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return manageProducts(type_of_user, user_id)


# Ver todos los productos disponibles en el archivo csv
def viewAllProducts(type_of_user: str, user_id: str):
  clear()

  products = readAllData("./data/producto.csv")
  loops = len(products)

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Juegos de Gameshop 🤓 !! "))
  print(drawUI(1, ""))
  print("*"*82)
  print()
  
  for i in range(0, loops, 2):
    p1 = products[i]
    p2 = None if(i == loops - 1 and loops % 2 != 0) else products[i+1]

    print("*"*40 + (("  " + "*"*40) if p2 else ""))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print(drawTables(1, {
      "p1": f" {p1.get('name')} ", 
      "p2": f" {p2.get('name')} " if p2 else None
      }))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print(drawTables(3, {
      "p1": f"Hecho en: {p1.get('filetype')}",
      "p2": f"Hecho en: {p2.get('filetype')}" if p2 else None
      }))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print(drawTables(3, {
      "p1": f"🆔 Id: {p1.get('id')}", 
      "p2": f"🆔 Id: {p2.get('id')}" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"👻 Categoría: {p1.get('category')}", 
      "p2": f"👻 Categoría: {p2.get('category')}" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"💰 Precio: S/. {p1.get('price')}.00",
      "p2": f"💰 Precio: S/. {p2.get('price')}.00" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"😎 Meta: {p1.get('goal')}", 
      "p2": f"😎 Meta: {p2.get('goal')}" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"🤑 Vendidos: {p1.get('selled')}",
      "p2": f"🤑 Vendidos: {p2.get('selled')}" if p2 else None
      }))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print("*"*40 + (("  " + "*"*40) if p2 else ""))
    print()
  
  opc = input("|| => 😮 Tipea 'A' para regresar: ").upper()
  print()

  match opc:
    case "A": return manageProducts(type_of_user, user_id)
    case _: 
      print("No válido, tipéalo nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return manageProducts(type_of_user, user_id)


# Agregar un juego nuevo
def createProduct(type_of_user: str, user_id: str):
  clear()

  print()
  print("*"*80)
  print(drawUI(1, ""))
  print(drawUI(1, f" Crea un nuevo juego para su venta 🎮 ! "))
  print(drawUI(1, ""))
  print(drawUI(2, "Crea los datos del producto:"))
  print(drawUI(1, ""))
  
  # id,filetype,name,goal,price,path,category,selled
  # register 
  filetype = input("|| => ¿El programa está en Python 🐍 o en Pseint 🤠 ?: ")
  name = input("|| => 🎮 ¿Cúal es el nombre del juego?: ")
  goal = input("|| => 👻 ¿Cúal es el objetivo del juego?: ")
  price = input("|| => 🤑 ¿Cúal es el precio del producto?: ")
  path = input("|| => 😎 ¿Cúal el nombre de su archivo?: ")
  category = input("|| => 👾 ¿Cúal es la categoría del producto?: ")

  row_count = 1

  new_product_data = {
    "id": f"P{row_count}",
    "filetype": filetype,
    "name": name,
    "goal": goal,
    "price": price,
    "path": path,
    "category": category,
    "selled": 0,
  }

  print(drawUI(1, ""))
  print("*"*80)
  print()

  lazyMessage("|| Verificando en ", 3)

  """
  # Hacer la verificación si el usuario existe
  result = searchByAttribute("username", username, "./data/cliente.csv")

  if(result is None):
    if(password == repeat_password):
      return infoCompletion(username, password)
    else: return errorFound("¡Las contraseñas ingresadas no coinciden!", "s1")
  else: 
    return errorFound("¡El usuario especificado ya existe!, ingrese un usuario diferente.", "s1")
  """

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