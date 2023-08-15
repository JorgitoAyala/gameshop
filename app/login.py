# importing files
from utils.console import drawUI, clear, lazyMessage
from api.general import searchByAttribute
from utils.security import decrypt

# Elección de inicio de sesión
def chooseRole():
  clear()

  print("**********************************************************************************")
  print("||          ________                             .__                            ||")
  print("||         /  _____/_____    _____   ____   _____|  |__   ____ ______           ||")
  print("||        /   \  ___\__  \  /     \_/ __ \ /  ___/  |  \ /  _ \ ____ \          ||")
  print("||        \    \_\  \/ __ \|  Y Y  \  ___/ \___ \|   Y  (  <_> )  |_> >         ||")
  print("||         \______  (____  /__|_|  /\___  >____  >___|  /\____/|   __/          ||")
  print("||                \/     \/      \/     \/     \/     \/       |__|             ||")
  print("||                                                                              ||")
  print("**********************************************************************************")
  
  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, " Bienvenido a Gameshop 😄 ! "))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Que rol de usuario tienes? 🤔"))
  print(drawUI(1, ""))
  print(drawUI(2, "A) Ingresa como administrador"))
  print(drawUI(2, "B) Ingresa como cliente"))
  print(drawUI(2, "C) Salir de la aplicación"))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Todavía no tienes una cuenta? 😱"))
  print(drawUI(2, "D) Regístrate como cliente ahora"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": return loginUI("administrador")
    case "B": return loginUI("cliente")
    case "C": return print("¡Muchas gracias por su visita 😄 !", end="\n\n")
    case "D": 
      from app.register import registerUI
      return registerUI()
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return chooseRole()


# Petición de datos de inicio de sesión
def loginUI(type_of_user: str):
  clear()

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" ¡Hola {type_of_user.capitalize()} 😄 ! "))
  print(drawUI(1, ""))
  print(drawUI(2, "Ingresa tus credenciales de inicio de sesión:"))
  print(drawUI(1, ""))
  username = input("|| => Usuario: ")
  password = input("|| => Contraseña: ")
  print(drawUI(1, ""))
  print("*"*82)
  print()

  lazyMessage("|| Verificando en ", 3)

  # Hacer la verificación si el usuario existe
  file_path = f"./data/{type_of_user}.csv"
  result = searchByAttribute("username", username, file_path)

  if(result is None):
    return errorFound(type_of_user, "El usuario no fue encontrado")
  else:
    if (decrypt(result.get("password")) != password):
      return errorFound(type_of_user, "La contraseña es incorrecta")
    else:
      from app.dashboard import userDashboard
      user_id = result.get("id")
      return userDashboard(type_of_user, user_id)


# En caso haya un error
def errorFound(type_of_user: str, type_of_error: str):

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, " Hay un error 🤬 !! "))
  print(drawUI(1, ""))
  print(drawUI(3, f"Mensaje: '{type_of_error}' 😯"))
  print(drawUI(1, ""))
  print(drawUI(2, "A) Intentar nuevamente"))
  print(drawUI(2, "B) Regresar al inicio de sesión"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": return loginUI(type_of_user)
    case "B": return chooseRole()
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      return errorFound(type_of_user, type_of_error)