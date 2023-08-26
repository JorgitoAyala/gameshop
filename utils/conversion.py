from datetime import datetime, date

# Obtener la cantidad de años apartir de la fecha de nacimiento
def getAgeByBirthday(birthday_string: str):
  # Convertir la cadena de fecha en un objeto de fecha (datetime)
  birthday_date = datetime.strptime(birthday_string, "%Y-%m-%d").date()

  # Obtener la fecha actual
  today_date = date.today()

  # Calcular la diferencia entre la fecha actual y la fecha de nacimiento
  age = today_date.year - birthday_date.year - ((today_date.month, today_date.day) < (birthday_date.month, birthday_date.day))

  return age


# Convertir de una cadena ("[P001-P002]") a lista (["P001", "P002"])
def fromStringToList(string_data: str):
  dataList = string_data[1:-1].split("-")

  return dataList


# Salto de linea de una cadena
def lineStringWrap(phrase, max_length):
  words = phrase.split()
  result = ""
  actual_line = ""
  
  for word in words:
    if len(actual_line) + len(word) + 1 <= max_length:
      actual_line += word + " "
    else:
      result += actual_line.strip() + "\n||    "
      actual_line = word + " "
  
  result += actual_line.strip()
  
  return result