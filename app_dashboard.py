# importing files
import utils
import textfiles

# Dashboard
def userDashboard(type_of_user: str, user_id: str):
  utils.clear()

  file_path = f"./data/{type_of_user}.csv"
  result = textfiles.searchByAttribute("id", user_id, file_path)

  print()
  print("********************************************************")
  print(utils.drawUI(1, ""))
  print(utils.drawUI(1, f" ¡Hola {result.get('fullname')}! "))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "¿Que deseas hacer?"))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "A) Ver mi perfil"))

  if(type_of_user == "cliente"):
    print(utils.drawUI(2, "B) Ver juegos disponibles"))
    print(utils.drawUI(2, "C) Mis juegos"))
  else:
    print(utils.drawUI(2, "B) Gestionar productos"))
    print(utils.drawUI(2, "C) Gestionar clientes"))

  print(utils.drawUI(2, "D) Cerrar sesión"))
  print(utils.drawUI(1, ""))
  print("********************************************************")
  print()

  opc = input("|| => Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": userProfile(type_of_user, user_id)
    case "B": print()
    case "C": print()
    case "D": 
      import gameshop
      gameshop.chooseRole()
    case _: 
      print("Seleccione una opción nuevamente!", end="\n\n")
      utils.lazyMessage("|| Reiniciando... => ")
      userDashboard(type_of_user, user_id)


# Configuración del perfil del usuario
def userProfile(type_of_user: str, user_id: str):
  utils.clear()

  file_path = f"./data/{type_of_user}.csv"
  result = textfiles.searchByAttribute("id", user_id, file_path)

  print()
  print("********************************************************")
  print(utils.drawUI(1, ""))
  print(utils.drawUI(1, " Información de tu perfil "))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, f"Nombre: {result.get('fullname')}."))
  print(utils.drawUI(2, f"Usuario: {result.get('username')}."))
  print(utils.drawUI(2, f"Contraseña: {result.get('password')}."))
  print(utils.drawUI(2, f"Email: {result.get('email')}."))
  print(utils.drawUI(2, f"Celular: {result.get('phone')}."))
  print(utils.drawUI(2, f"DNI: {result.get('dni')}."))
  print(utils.drawUI(2, f"Fecha de nacimiento: {result.get('birthday')}."))
  print(utils.drawUI(2, f"Edad: {utils.getAgeByBirthday(result.get('birthday'))} años."))
  print(utils.drawUI(2, f"Dirección: {result.get('address')}."))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "¿Que deseas hacer?"))
  print(utils.drawUI(1, ""))
  print(utils.drawUI(2, "A) Actualizar mi nombre completo"))
  print(utils.drawUI(2, "B) Actualizar mi usuario"))
  print(utils.drawUI(2, "C) Actualizar mi contraseña"))
  print(utils.drawUI(2, "D) Actualizar mi email"))
  print(utils.drawUI(2, "E) Actualizar mi celular"))
  print(utils.drawUI(2, "F) Actualizar mi DNI"))
  print(utils.drawUI(2, "G) Actualizar mi fecha de nacimiento"))
  print(utils.drawUI(2, "H) Actualizar mi dirección"))
  print(utils.drawUI(2, "I) Regresar al dashboard"))
  print(utils.drawUI(1, ""))
  print("********************************************************")
  print()

  opc = input("|| => Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": print()
    case "B": print()
    case "C": print()
    case "D": print()
    case "E": print()
    case "F": print()
    case "G": print()
    case "H": print()
    case "I": userDashboard(type_of_user, user_id)
    case _: 
      print("Seleccione una opción nuevamente!", end="\n\n")
      utils.lazyMessage("|| Reiniciando... => ")
      userProfile(type_of_user, user_id)


# Configuración del perfil del usuario
def changeProfile(user_id: str, update_key: str, updated_name: str, file_path: str):

  print()
  print("********************************************************")
  print(utils.drawUI(1, ""))
  print(utils.drawUI(1, f" Actualizar {updated_name} "))
  print(utils.drawUI(1, ""))
  update_value = input("|| => Ingrese valor: ")
  print(utils.drawUI(1, ""))
  print("********************************************************")
  print()

  textfiles.updateData(user_id, update_key, update_value, file_path)