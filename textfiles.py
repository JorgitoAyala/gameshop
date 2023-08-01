import csv

# Crear datos en el archivo .csv seleccionado
def createData(file_path, headers, data):

  with open(file_path, mode="a", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)

    # Verificar si el documento .csv está vacío
    if csv_file.tell() == 0:
      writer.writeheader()

    writer.writerows(data)


# Leer todos los datos del archivo .csv seleccionado
def readData(file_path):
  
  data = []
  
  with open(file_path, mode="r") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
      data.append(row)
  
  return data


"""
FUNCIONES EN GENERAL
"""
# Buscar un dato en particular por un atributo en especifico
def searchByAttribute(search_type: str, search_value: str, filename: str):
  with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Buscar la fila correspondiente al atributo en especifico
    for row in csvreader:
      if row[search_type] == search_value:
        return row

    return None

# Actualizar un dato en particular por un id en específico
def updateData(value_id: str, update_key: str, update_value: str, filename: str):
  # Leer el contenido del archivo CSV y cargarlo en una lista de diccionarios
  with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = [row for row in csvreader]

  # Buscar la fila en la lista de diccionarios que corresponde al nombre a buscar
  for row in data:
    if row['id'] == value_id:
      row[update_key] = update_value
      break

  # Escribir la lista actualizada de diccionarios nuevamente en el archivo CSV
  with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=csvreader.fieldnames)
    csvwriter.writeheader()
    csvwriter.writerows(data)


"""
FUNCIONES PARA ADMINISTRADORES
"""

"""
FUNCIONES PARA CLIENTES
"""

"""
FUNCIONES PARA PRODUCTOS
"""