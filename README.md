# equipouno

#proyeto 1 
# Proyecto: Analisis de transacciones
# Autor: carlos enrique guerra rivera 
# Fecha: 28/02/2026

print("Analisis de datos iniciado...")

archivo = "SAML-D_145_datos.csv"

with open(archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()

print("Total de registros:", len(lineas) - 1)
print("Proceso finalizado correctamente.")

