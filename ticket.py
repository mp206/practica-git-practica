def calcular_total():
    total = 0
    while True:
        # Solicitar el nombre del producto
        producto = input("Ingresa el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break

        # Solicitar la cantidad y el precio
        try:
            cantidad = int(input(f"¿Cuántos {producto} compraste? "))
            precio = float(input(f"¿Cuál es el precio de un {producto}? "))
        except ValueError:
            print("Entrada no válida. Intenta de nuevo.")
            continue

        # Calcular el total por producto y acumularlo
        total += cantidad * precio
        print(f"El total por {producto} es: {cantidad * precio:.2f}")
    
    # Mostrar el total final
    print(f"\nEl total de tu compra es: {total:.2f}")

# Llamar a la función
calcular_total()