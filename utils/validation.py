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

    case _:
      return print("CODE ERROR: ¡No existe el tipo de validación!")

  valid = re.match(pattern, value) is not None
  
  return {
    "v": valid,
    "m": "¡Se ha validado correctamente 😄 !" if valid else message
  }


def validationProduct(value: str, validation_type: str):
  
  print()


def validationBankingCard(value: str, validation_type: str):
  value = value.encode("latin-1").decode("utf-8")

  match validation_type:

    case "visa":
      pattern = r"^4[0-9]{12}(?:[0-9]{3})?$"
      message = "La tarjeta Visa comienza con el dígito 4, seguido de 12 dígitos numéricos y opcionalmente 3 dígitos adicionales al final."

    case "mastercard":
      pattern = r"^5[1-5][0-9]{14}$"
      message = "La tarjeta MasterCard comienza con 51 a 55, seguido de 14 dígitos numéricos."

    case "discover":
      pattern = r"^6(?:011|5[0-9][0-9])[0-9]{12}$"
      message = "La tarjeta Discover, comienza con 6011 o con 65 seguido de dos dígitos entre 00 y 99, y luego 12 dígitos numéricos adicionales"
      
    case "american_express":
      pattern = r"^3[47][0-9]{13}$"
      message = "La tarjeta American Express comienza con 34 o 37, seguido de 13 dígitos numéricos."
      
    case "diners_club":
      pattern = r"3(?:0[0-5]|[68][0-9])[0-9]{11}$"
      message = "La tarjeta Diners Club comienza con 30 a 36, o con 38 o 39, seguido de 11 dígitos numéricos adicionales."
      
    case "jcb":
      pattern = r"^(?:2131|1800|35\d{3})\d{11}$"
      message = "La tarjeta JCB comienza con 2131, 1800 o 35 seguido de tres dígitos, y luego 11 dígitos numéricos adicionales."
    
    case "date_number":
      pattern = r"^(0[1-9]|1[0-2])\/(1[9-9]|2[0-9])$"
      message = "La tarjeta bancaria debe tener exactamente el formato de fecha adecuado para poder realizar la transacción del dinero correctamente!"

    case "cvv2_number":
      pattern = r"^(?!000)\d{3,4}$"
      message = "El CVV2 de la tarjeta bancaria según el tipo de tarjeta debe tener de 3 a 4 números que sirven para poder validar la tarjeta satisfactoriamente!"

    case _:
      return print("CODE ERROR: ¡No existe el tipo de validación!")
  
  valid = re.match(pattern, value) is not None
  
  return {
    "v": valid,
    "m": "¡Se ha validado correctamente 😄 !" if valid else message
  }

