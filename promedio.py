def calcular_promedio(lista):
    if not lista:  # Verificar si la lista está vacía
        return None
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

# Ejemplo de uso
numeros = [10, 15, 20, 25, 30]
promedio = calcular_promedio(numeros)
if promedio is not None:
    print("El promedio de la lista es:", promedio)
else:
    print("La lista está vacía.")
