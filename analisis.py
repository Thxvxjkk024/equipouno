# Proyecto: Analisis de Transacciones
# Equipo: Equipo 1
# Administrador: Thelma Getzemani Avila Martinez
# Fecha: 28/02/2026
# Descripción: Resolución de conflicto e integración final del archivo de datos.


# Iniciales: N. G. F. E.
# Fecha de modificación: 28 de febrero de 2026
# Comentario: Script inicial para la lectura y exploración del dataset del equipo.

print("--- Comenzando el analizis de datos ---")  # Cambie a Comenzando Autor:Carlos enrique guerra rivera 28/02/2026
print("Buscando el archivo 'datos.csv' generado por el Colaborador A...")
print("Carga de datos simulada y análisis preliminar completado con éxito.")

# Nota para el futuro: Aquí usaremos librerías como Pandas para limpiar los datos reales.

# Modificado:carlos enrique guerra rivera
# Fecha: 28/02/2026

print("Revision realizada por colaborador A.")

# Proyecto: Analisis de Transacciones
# Autor: carlos enrique guerra rivera
# Fecha: 28/02/2026

archivo = "SAML-D_145_datos.csv"

with open(archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()

total_registros = len(lineas) - 1  # se resta el encabezado

print("Total de registros:", total_registros)
