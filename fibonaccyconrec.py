
def fibonacci_recursivo(n):
    """Devuelve el n-ésimo término de Fibonacci usando recursividad."""
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def main():
    print("     SERIE DE FIBONACCI (Recursiva)")
    n = int(input("Ingresa la cantidad de términos: "))

    if n <= 0:
        print("Debes ingresar un número entero positivo.")
    else:
        print("\nSerie generada:")
        for i in range(n):
            print(fibonacci_recursivo(i), end=" ")
        print("\n\nPrograma finalizado correctamente.")


if __name__ == "__main__":
    main()
