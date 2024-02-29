def tabla_multiplicar(n, m):
    tabla = []
    for i in range(1, m+1):
        fila = []
        for j in range(1, n+1):
            fila.append(i * j)
        tabla.append(fila)
    return tabla

def imprimir_tabla(tabla):
    for fila in tabla:
        print("\t".join(map(str, fila)))

# Solicitar al usuario el tamaño de la tabla
n = int(input("Ingrese el número de columnas de la tabla de multiplicar: "))
m = int(input("Ingrese el número de filas de la tabla de multiplicar: "))

# Generar la tabla de multiplicar
mi_tabla = tabla_multiplicar(n, m)

# Imprimir la tabla
imprimir_tabla(mi_tabla)
