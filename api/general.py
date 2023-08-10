import csv

# Buscar un dato en particular por un atributo en especifico
def searchByAttribute(search_type: str, search_value: str, filename: str):
  with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Buscar la fila correspondiente al atributo en especifico
    for row in csvreader:
      if row[search_type] == search_value:
        return row

    return None


# Crear un nuevo registro en el archivo .csv
def addData(filename: str, data: dict):
  with open(filename, 'a', newline='') as csvfile:
    fieldnames = data.keys()
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writerow(data)


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

    return None


# Obtener la cantidad de filas de un documento particular
def getQuantity(filename:str):
  with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    row_counter = sum(1 for row in csvreader)
  return row_counter