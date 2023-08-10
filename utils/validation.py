import re

def validationInfo(value: str, validation_type: str):

  value = value.encode("latin-1").decode("utf-8")

  match validation_type:

    case "fullname":
      pattern = r"^[A-Za-záéíóúñÁÉÍÓÚÑ']+([ -][A-Za-záéíóúñÁÉÍÓÚÑ']+)*$"
      message = "El nombre completo debe contener solo letras, pueden ser mayúsculas minúsculas con o sin tildes."

    case "username":
      pattern = r"^(?=.*[A-Z]).{6,}$"
      message = "El usuario debe contener mínimo 6 caracteres, una mayúscula y una minúscula. Puede tener letras, números y caracteres especiales."

    case "password":
      pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%^&*()_+={}[\]:;<>,.?~\-])\S{8,}$"
      message = "La contraseña debe contener mínimo 8 caracteres, al menos una mayúscula, una minúscula, un carácter especial y un número."

    case "email":
      pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
      message = "El email debe contener una estructura válida como el ejemplo siguiente: usuario@example.com"

    case "phone":
      pattern = r"^9\d{8}$"
      message = "El celular debe contener tener estrictamente 9 números, empezando por el 9."

    case "dni":
      pattern = r"^\d{8}$"
      message = "El DNI debe contener tener estrictamente 8 números."

    case "birthday":
      pattern = r"^(?:(?:19|20)\d\d)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
      message = "La fecha de nacimiento debe contener una estructura válida (YYYY-MM-DD) como el ejemplo siguiente: 2001-10-23"

    case "banking_card":
      pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$"
      message = "La tarjeta bancaria debe contener los parametros regulatorios según el tipo de tarjeta que se trate (Visa, MasterCard, American Express, Discover o Diners Club)"

    case _:
      return print("CODE ERROR: ¡No existe el tipo de validación!")

  valid = re.match(pattern, value) is not None
  
  return {
    "v": valid,
    "m": "¡Se ha validado correctamente 😄 !" if valid else message
  }