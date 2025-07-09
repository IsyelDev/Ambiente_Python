with open("Base_Características_Crédito_0.csv", "r", encoding="latin") as csv_file:
  reader = csv.DictReader(csv_file)
  for row in reader:
    print(row['PRODUCTO'], row['DEPARTAMENTO'])

fieldnames = ["Nombre", "Edad", "Ciudad"]

with open("dict_output.csv", "w", newline="", encoding="utf-8") as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({"Nombre": "Eve", "Edad": 26, "Ciudad": "Miami"})
  writer.writerow({"Nombre": "Frank", "Edad": 31, "Ciudad": "Houston"})

with open("output.csv", "w", newline="", encoding="utf-8") as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(["Nombre", "Edad", "Ciudad"]) # header
  writer.writerow(["Charlie", 22, "Boston"])
  writer.writerow(["Diana", 28, "Chicago"])

def clasificar_valores(**kwargs):
    numeros = []
    textos = []
    otros = []
    for v in kwargs.values():
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            numeros.append(v)
        elif isinstance(v, str):
            textos.append(v)
        else:
            otros.append(v)
    return numeros, textos, otros
