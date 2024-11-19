from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Bienvenido a la Calculadora")
    print("Seleccione una opción:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada de N números")
    print("6. Salir")

while True:
    menu()
    opcion = input("Ingrese una opción: ")
    
    if opcion == '1':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = sumar(a, b)
        print(f"El resultado de la suma es: {resultado}\n")
    elif opcion == '2':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = restar(a, b)
        print(f"El resultado de la resta es: {resultado}\n")
    elif opcion == '3':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = multiplicar(a, b)
        print(f"El resultado de la multiplicación es: {resultado}\n")
    elif opcion == '4':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador: "))
        resultado = dividir(a, b)
        print(f"El resultado de la división es: {resultado}\n")
    elif opcion == '5':
        numeros = input("Ingrese los números a sumar separados por espacio: ")
        numeros = list(map(float, numeros.strip().split()))
        resultado = suma_avanzada(*numeros)
        print(f"El resultado de la suma avanzada es: {resultado}\n")
    elif opcion == '6':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.\n")
