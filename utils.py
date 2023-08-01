from datetime import datetime, date
from time import sleep
import base64
import re
import os

# Para crear un mensaje con retardo especifico
def lazyMessage(word: str):
  print(word, end=" ")

  for second in range(3, 0, -1):
    print(second, end=" ", flush=True)
    sleep(1)
  
  print("... Listo!", end="\n")


# Para limpiar la consola
def clear():
  if os.name == "nt": 
    os.system("cls")
  else: 
    os.system("clear")


# Para pintar una linea de la consola de un determinado patrón
def drawUI(typeTable: int, phrase: str):
  match typeTable:

    case 1:
      chars = round((50 - len(phrase)) / 2)
      return f'|| {"=" * chars}{phrase}{"=" * chars} ||'
    
    case 2:
      chars = 50 - len(phrase)
      return f'|| {phrase}{" " * chars} ||'
    
    case _:
      return "Hay un error"


# Obtener la cantidad de años apartir de la fecha de nacimiento
def getAgeByBirthday(birthday_string: str):
  # Convertir la cadena de fecha en un objeto de fecha (datetime)
  birthday_date = datetime.strptime(birthday_string, "%Y-%m-%d").date()

  # Obtener la fecha actual
  today_date = date.today()

  # Calcular la diferencia entre la fecha actual y la fecha de nacimiento
  age = today_date.year - birthday_date.year - ((today_date.month, today_date.day) < (birthday_date.month, birthday_date.day))

  return age


# Convertir de una cadena ("[P001, P002]") a lista (["P001", "P002"])
def fromStringToList(string_data: str):
  dataList = string_data[1:-1].split(", ")

  return dataList


# Para encriptar contraseñas
def encrypt(text: str):
  # Condifica el texto en base64
  encoded_bytes = base64.b64encode(text.encode('utf-8'))

  # Convierte los bytes de nuevo en una cadena
  encrypted_text = encoded_bytes.decode('utf-8')

  return encrypted_text

# Para desencriptar contraseñas
def decrypt(encrypted_text: str):
  # Decodificar el texto codificado en base64 a bytes
  decoded_bytes = base64.b64decode(encrypted_text.encode('utf-8'))

  # Convierte los bytes de nuevo en una cadena
  decrypted_text = decoded_bytes.decode('utf-8')

  return decrypted_text


"""
VALIDACIONES
"""
# Validar usuario
def validUsername(username):
  # Regex: Que contenga mínimo 6 caracteres, una mayúscula y una minúscula y puede tener letras, números y caracteres especiales.
  pattern = r"^(?=.*[A-Z]).{6,}$"
  
  return re.match(pattern, username) is not None

# Validar contraseña
def validPassword(password: str):
  # Regex: Que tenga mínimo 8 caracteres, que contenga al menos una mayúscula, una minúscula, un carácter especial y un número.
  pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%^&*()_+={}[\]:;<>,.?~\-])\S{8,}$"
  
  return re.match(pattern, password) is not None

# Validar correo electrónico
def validEmail(email: str):
  # Ejemplo de correo valido: usuario@gmail.com.pe
  pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  
  return re.match(pattern, email) is not None

# Validar número de celular
def validPhone(phone: str):
  # Ejemplo de número de celular válido: 999214556
  pattern = r"^9\d{8}$"

  return re.match(pattern, phone) is not None

# Validar nombre completo
def validFullName(fullname: str):
  # Expresión regular para validar nombre completo
  pattern = r"^[A-Za-záéíóúñÁÉÍÓÚÑ']+([ -][A-Za-záéíóúñÁÉÍÓÚÑ']+)*$"
  
  return re.match(pattern, fullname) is not None

# Validar DNI
def validDNI(dni: str):
  # Expresión regular para validar el DNI de Perú
  pattern = r"^\d{8}$"

  return re.match(pattern, dni) is not None

# Validar Tarjeta bancaria
def validBankingCard(banking_card: str):
  # Expresión regular para validar números de tarjetas bancarias
  # Visa, MasterCard, American Express, Discover y Diners Club
  pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$"
  
  return re.match(pattern, banking_card) is not None