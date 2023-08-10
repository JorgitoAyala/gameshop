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