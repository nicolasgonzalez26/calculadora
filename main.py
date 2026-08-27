def multiplicacion(numero1, numero2):
    return numero1 * numero2


print("=================================")
print("   CALCULADORA DE MULTIPLICACIÓN")
print("=================================")

while True:
    try:
        numero1 = float(input("\nIngrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        resultado = multiplicacion(numero1, numero2)

        print(f"\nResultado: {numero1} × {numero2} = {resultado}")

        continuar = input("\n¿Desea realizar otra multiplicación? (s/n): ").lower()

        if continuar != "s":
            print("\nGracias por usar la calculadora.")
            break

    except ValueError:
        print("\nError: debe ingresar números válidos.")