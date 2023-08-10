# importing files
from utils.console import drawUI, clear, lazyMessage
from api.general import searchByAttribute, getQuantity, addData
from utils.security import encrypt, decrypt
from utils.validation import validationInfo
from utils.conversion import getAgeByBirthday, lineStringWrap

# PASO 1: Creación de credenciales de inicio de sesión
def registerUI():
  clear()

  print()
  print("**************************************************************")
  print(drawUI(1, ""))
  print(drawUI(1, f" Regístrate como nuevo cliente 😁 ! "))
  print(drawUI(1, ""))
  print(drawUI(2, "Crea credenciales de inicio de sesión:"))
  print(drawUI(1, ""))
  # register username
  username = input("|| => 😁 Crea un usuario: ")
  validInfo = validationInfo(username, "username")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s1")
  # register password
  password = input("|| => 🔒 Crea una contraseña: ")
  validInfo = validationInfo(password, "password")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s1")
  # register repeat password
  repeat_password = input("|| => 🔏 Repite la contraseña: ")
  validInfo = validationInfo(repeat_password, "password")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s1")
  print(drawUI(1, ""))
  print("**************************************************************")
  print()

  lazyMessage("|| Verificando en ", 3)

  # Hacer la verificación si el usuario existe
  result = searchByAttribute("username", username, "./data/cliente.csv")

  if(result is None):
    if(password == repeat_password):
      return infoCompletion(username, password)
    else: return errorFound("¡Las contraseñas ingresadas no coinciden!", "s1")
  else: 
    return errorFound("¡El usuario especificado ya existe!, ingrese un usuario diferente.", "s1")


# PASO 2: Completitud de datos adicionales de perfil:
def infoCompletion(username: str, password: str):
  print()
  print("**************************************************************")
  print(drawUI(1, ""))
  print(drawUI(1, f" Ahora completa los datos de tu perfil 😄 "))
  print(drawUI(1, ""))
  print(drawUI(2, "Ingresa los siguientes datos requeridos:"))
  print(drawUI(1, ""))
  # register fullname
  fullname = input("|| => 😄 Nombre completo: ")
  validInfo = validationInfo(fullname, "fullname")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s2")
  # register email
  email = input("|| => 📧 Correo electrónico: ")
  validInfo = validationInfo(email, "email")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s2")
  # register phone
  phone = input("|| => 📱 Celular: ")
  validInfo = validationInfo(phone, "phone")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s2")
  # register dni
  dni = input("|| => 🆔 DNI: ")
  validInfo = validationInfo(dni, "dni")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s2")
  # register address
  address = input("|| => 🏠 Dirección: ")
  # register birthday
  birthday = input("|| => 👶 Fecha de nacimiento: ")
  validInfo = validationInfo(birthday, "birthday")
  if(not(validInfo.get("v"))): return errorFound(validInfo.get("m"), "s2")
  print(drawUI(1, ""))
  print("**************************************************************")
  print()

  # Validación exitosa
  if(validInfo.get("v")):
    filename = "./data/cliente.csv"
    row_count = getQuantity(filename)

    new_client_data = {
      "id": f"C{row_count}",
      "username": username,
      "password": encrypt(password),
      "fullname": fullname,
      "email": email,
      "phone": phone,
      "dni": dni,
      "address": address,
      "birthday": birthday,
      "games": "[]"
    }

    addData(filename, new_client_data)

    print(f"|| {validInfo.get('m')}")

    print()
    print("**************************************************************")
    print(drawUI(1, ""))
    print(drawUI(1, " Felicitaciones!, creó su cuenta satisfactoriamente! 🎉 "))
    print(drawUI(1, ""))
    print("**************************************************************")
    print()

    lazyMessage("|| Será redirigido al inicio de sesión en ", 7)

    from app.login import chooseRole
    return chooseRole()


# En caso haya un error, step1 (s1) - step2 (s2)
def errorFound(type_of_error: str, step: str):
  print()
  print("**************************************************************")
  print(drawUI(1, ""))
  print(drawUI(1, " Hay un error 🤬 !! "))
  print(drawUI(1, ""))
  print(lineStringWrap(f"|| => Mensaje: '{type_of_error}' 😯", 50))
  print(drawUI(1, ""))
  print(drawUI(2, "A) Intentar nuevamente"))
  print(drawUI(2, "B) Regresar al inicio de sesión"))
  print(drawUI(1, ""))
  print("**************************************************************")
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": 
      if(step == "s1"): return registerUI()
      elif(step == "s2"): return infoCompletion()
      else: return print("CODE ERROR: No hay opción!")
    case "B": 
      from app.login import chooseRole
      return chooseRole()
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      return errorFound(type_of_error, step)