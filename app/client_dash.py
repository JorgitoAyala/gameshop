# importing files
from utils.console import drawUI, clear, lazyMessage
from api.general import searchByAttribute, getQuantity, addData
from utils.security import encrypt
from utils.validation import validationInfo
from utils.conversion import lineStringWrap

# Dashboard del usuario OPCION 1: Juegos disponibles
def availableGames(type_of_user: str, user_id: str):
  clear()

  client_info = searchByAttribute("id", user_id, "./data/cliente.csv")

  print()
  print("*"*80)
  print(drawUI(1, ""))
  print(drawUI(1, f" Juegos disponibles 😁🎮 "))
  print(drawUI(1, ""))
  print(drawUI(2, "Crea credenciales de inicio de sesión:"))
  print(drawUI(1, ""))


# Dashboard del usuario OPCION 2: Mis Juegos comprados
def myGames(type_of_user: str, user_id: str):
  print()