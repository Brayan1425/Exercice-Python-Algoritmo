def fibonacci(n):
    fibonacci_series = [0, 1]  # Iniciamos con los primeros dos números de la serie

    while len(fibonacci_series) < n:
        # Calculamos el siguiente número de la serie sumando los dos últimos
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series

# Solicitamos al usuario el número de términos que desea generar
numero_terminos = int(input("Ingrese el número de términos de la serie de Fibonacci que desea generar: "))

# Generamos la serie de Fibonacci
resultado = fibonacci(numero_terminos)

# Mostramos la serie de Fibonacci generada
print("La serie de Fibonacci con", numero_terminos, "términos es:")
print(resultado)
