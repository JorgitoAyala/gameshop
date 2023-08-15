# importing files
from utils.console import drawUI, clear, lazyMessage
from utils.conversion import getAgeByBirthday, lineStringWrap
from utils.validation import validationInfo
from utils.security import encrypt, decrypt
from api.general import searchByAttribute, updateData

# Dashboard
def userDashboard(type_of_user: str, user_id: str):
  clear()

  file_path = f"./data/{type_of_user}.csv"
  result = searchByAttribute("id", user_id, file_path)

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Hola {result.get('fullname')} 😄 ! "))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Que deseas hacer? 🤔"))
  print(drawUI(1, ""))
  print(drawUI(3, "A) Ver mi perfil 😄"))

  if(type_of_user == "cliente"):
    print(drawUI(3, "B) Ver juegos disponibles 🎮"))
    print(drawUI(3, "C) Mis juegos 👾"))
  else:
    print(drawUI(3, "B) Gestionar productos 🤓"))
    print(drawUI(3, "C) Gestionar clientes 🧑‍🤝‍🧑"))

  print(drawUI(3, "D) Cerrar sesión 😮"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": userProfile(type_of_user, user_id)
    case "B":
      if(type_of_user == "cliente"):
        from app.client_dash import availableGames
        return availableGames(type_of_user, user_id)
      else:
        from app.admin_dash import manageProducts
        return manageProducts(type_of_user, user_id)
    case "C": 
      if(type_of_user == "cliente"):
        from app.client_dash import myGames
        return myGames(type_of_user, user_id)
      else:
        from app.admin_dash import manageProducts
        return manageProducts(type_of_user, user_id)
    case "D":
      from app.login import chooseRole
      return chooseRole()
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return userDashboard(type_of_user, user_id)


# Configuración del perfil del usuario
def userProfile(type_of_user: str, user_id: str):
  clear()

  file_path = f"./data/{type_of_user}.csv"
  result = searchByAttribute("id", user_id, file_path)

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, " Información de tu perfil: 😁 "))
  print(drawUI(1, ""))
  print(drawUI(3, f"😄 Nombre: {result.get('fullname')}."))
  print(drawUI(3, f"😁 Usuario: {result.get('username')}."))
  print(drawUI(3, f"🔒 Contraseña: {result.get('password')}."))
  print(drawUI(3, f"📧 Email: {result.get('email')}."))
  print(drawUI(3, f"📱 Celular: {result.get('phone')}."))
  print(drawUI(3, f"🆔 DNI: {result.get('dni')}."))
  print(drawUI(3, f"👶 Fecha de nacimiento: {result.get('birthday')}."))
  print(drawUI(3, f"😛 Edad: {getAgeByBirthday(result.get('birthday'))} años."))
  print(drawUI(3, f"🏠 Dirección: {result.get('address')}."))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Que deseas hacer? 🤔"))
  print(drawUI(1, ""))
  print(drawUI(2, "A) Actualizar mi nombre completo"))
  print(drawUI(2, "B) Actualizar mi usuario"))
  print(drawUI(2, "C) Actualizar mi contraseña"))
  print(drawUI(2, "D) Actualizar mi email"))
  print(drawUI(2, "E) Actualizar mi celular"))
  print(drawUI(2, "F) Actualizar mi DNI"))
  print(drawUI(2, "G) Actualizar mi fecha de nacimiento"))
  print(drawUI(2, "H) Actualizar mi dirección"))
  print(drawUI(3, "I) Regresar al dashboard 😮"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": return changeProfile(type_of_user, user_id, "fullname", file_path, "Nombre completo")
    case "B": return changeProfile(type_of_user, user_id, "username", file_path, "Usuario")
    case "C": return changeProfile(type_of_user, user_id, "password", file_path, "Contraseña")
    case "D": return changeProfile(type_of_user, user_id, "email", file_path, "Email")
    case "E": return changeProfile(type_of_user, user_id, "phone", file_path, "Celular")
    case "F": return changeProfile(type_of_user, user_id, "dni", file_path, "DNI")
    case "G": return changeProfile(type_of_user, user_id, "birthday", file_path, "Fecha de nacimiento")
    case "H": return changeProfile(type_of_user, user_id, "address", file_path, "Dirección")
    case "I": return userDashboard(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return userProfile(type_of_user, user_id)


# Configuración del perfil del usuario
def changeProfile(type_of_user: str, user_id: str, update_key: str, file_path: str, updated_name: str):
  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Actualizar {updated_name} 🤓 !! "))
  print(drawUI(1, ""))
  update_value = input(f"|| => Ingrese {updated_name}: ")
  print(drawUI(1, ""))
  print("*"*82)
  print()

  validation = validationInfo(update_value, update_key).get("v")
  message = validationInfo(update_value, update_key).get("m")

  if(validation):
    if(passwordAuthentication(user_id, file_path)):
      if(update_key == "password"):
        updateData(user_id, update_key, encrypt(update_value), file_path)
      else: updateData(user_id, update_key, update_value, file_path)
      print(f"¡La información ha sido actualizada exitósamente 😄 !")
    else:
      print(f"No puede realizar cambios si la contraseña no es correcta 🤬 !")
      print(f"Intente el proceso nuevamente 😐 ...")
    
    print()
    lazyMessage("|| Reiniciando en ", 3)
    return userProfile(type_of_user, user_id)
  else: 
    return errorFound(message, type_of_user, user_id, update_key, file_path, updated_name)


# Verificar pidiendo la contraseña para realizar cambios
def passwordAuthentication(user_id: str, file_path: str):
  result = searchByAttribute("id", user_id, file_path)

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Antes de hacer cambios, verificar contraseña: 🤫 "))
  print(drawUI(1, ""))
  my_password = input(f"|| => 🔒 Ingresa tu contraseña: ")
  print(drawUI(1, ""))
  print("*"*82)
  print()

  return decrypt(result.get("password")) == my_password


# En caso haya un error
def errorFound(message: str, type_of_user: str, user_id: str, update_key: str, file_path: str, updated_name: str):
  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, " Hay un error 🤬 !! "))
  print(drawUI(1, ""))
  print(lineStringWrap(f"|| => {message} 😯", 50))
  print(drawUI(1, ""))
  print(drawUI(2, "A) Intentar nuevamente"))
  print(drawUI(2, "B) Regresar al perfil de usuario"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": return changeProfile(type_of_user, user_id, update_key, file_path, updated_name)
    case "B": return userProfile(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      return errorFound(message, type_of_user, user_id, update_key, file_path, updated_name)
