import pandas as pd

# Leer la hoja USO del archivo
df = pd.read_excel("Metales_IndRef.xlsx", sheet_name="USO")

# Diccionario final
datos = {}

# Guardar las longitudes de onda
datos["lambda"] = df["lambda"].tolist()

# Para cada columna de n/k, agrupar por elemento
for col in df.columns:
    if col == "lambda":
        continue  # ya la hemos guardado

    prop = col[0]      # 'n' o 'k'
    elem = col[1:]     # 'Au', 'Ag', 'Al', 'Cu', 'Pt', 'Zn', 'Fe', etc.

    if elem not in datos:
        datos[elem] = {}

    datos[elem][prop] = df[col].tolist()

with open("datos_metales.txt", "w") as f:
    f.write("datos_metales = ")
    for i in datos:
        f.write(repr(datos[i]) + "\n")
# Ejemplo de acceso:
# datos["Au"]["n"]  -> lista de nAu
# datos["Au"]["k"]  -> lista de kAu
# datos["lambda"]   -> lista de lambda
