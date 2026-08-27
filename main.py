<<<<<<< HEAD
num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))
division = num1 / num2
print("El resultado es: ", division)
=======
def multiplicacion(numero1, numero2):
    return numero1 * numero2

<<<<<<< HEAD
print(multiplicacion(5, 4))
>>>>>>> 6b0357a (Agrega funcion de multiplicacion)
=======

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
>>>>>>> 0dcdc1c (Mejora calculadora de multiplicacion interactiva)
