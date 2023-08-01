# importing files
import utils
import textfiles

logo_gameshop = """
                                    .__                   
   _________    _____   ____   _____|  |__   ____ ______  
  / ___\__  \  /     \_/ __ \ /  ___/  |  \ /  _ \\\\____ \ 
 / /_/  > __ \|  Y Y  \  ___/ \___ \|   Y  (  <_> )  |_> >
 \___  (____  /__|_|  /\___  >____  >___|  /\____/|   __/ 
/_____/     \/      \/     \/     \/     \/       |__|    

"""

# Elección de inicio de sesión
def chooseRole():
  utils.clear()

  print("********************************************************")
  print(logo_gameshop)
  print("********************************************************")
  
  print()
  print("********************************************************")
  print(utils.drawUI(1, ""))
  print(utils.drawUI(1, " BIENVENIDO A GAMESHOP! "))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "¿Que rol de usuario tienes?"))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "A) Administrador"))
  print(utils.drawUI(2, "B) Cliente"))
  print(utils.drawUI(2, "C) Salir"))
  print(utils.drawUI(1, ""))
  print("********************************************************")
  print()

  opc = input("|| => Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": loginUI("administrador")
    case "B": loginUI("cliente")
    case "C": print("Muchas gracias por su visita!")
    case _: 
      print("Seleccione una opción nuevamente!", end="\n\n")
      utils.lazyMessage("|| Reiniciando... => ")
      chooseRole()


# Petición de datos de inicio de sesión
def loginUI(type_of_user: str):
  utils.clear()

  print()
  print("********************************************************")
  print(utils.drawUI(1, ""))
  print(utils.drawUI(1, f" ¡HOLA {type_of_user.upper()}! "))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "Ingresa tus credenciales:"))
  print(utils.drawUI(1, ""))
  username = input("|| => Usuario: ")
  password = input("|| => Contraseña: ")
  print(utils.drawUI(1, ""))
  print("********************************************************")
  print()

  utils.lazyMessage("|| Verificando... => ")

  # Hacer la verificación si el usuario existe
  file_path = f"./data/{type_of_user}.csv"
  result = textfiles.searchByAttribute("username", username, file_path)

  if(result is None):
    errorFound(type_of_user, "El usuario no fue encontrado")
  else:
    if (result.get("password") != password):
      errorFound(type_of_user, "La contraseña es incorrecta")
    else:
      import app_dashboard
      user_id = result.get("id")
      app_dashboard.userDashboard(type_of_user, user_id)


# En caso haya un error
def errorFound(type_of_user: str, type_of_error: str):

  print()
  print("********************************************************")
  print(utils.drawUI(1, ""))
  print(utils.drawUI(1, " ERROR! "))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, f"{type_of_error}:"))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "A) Intentar nuevamente"))
  print(utils.drawUI(2, "B) Regresar al inicio de sesión"))
  print(utils.drawUI(1, ""))
  print("********************************************************")
  print()

  opc = input("|| => Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": loginUI(type_of_user)
    case "B": chooseRole()
    case _: 
      print("Seleccione una opción nuevamente!", end="\n\n")
      errorFound(type_of_user, type_of_error)


# EL INICIO DE LA APLICACIÓN
chooseRole()