
def generar_fibonacci_iterativo(n):
    """Genera la serie de Fibonacci de forma iterativa."""
    serie = []
    a, b = 0, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie


def main():
    print("     SERIE DE FIBONACCI ")
    n = int(input("Ingresa la cantidad de términos: "))

    if n <= 0:
        print("Debes ingresar un número entero positivo.")
    else:
        serie = generar_fibonacci_iterativo(n)
        print("\nSerie generada:")
        for numero in serie:
            print(numero, end=" ")
        print("\n\nPrograma finalizado correctamente.")


if __name__ == "__main__":
    main()
