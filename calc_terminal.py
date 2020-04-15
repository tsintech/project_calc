#Proyecto Parte 1 - Calculadora en terminal
#MIGUEL ANGEL CONDORI QUISPE
import time
sw = True
while sw:
    print('''
    Menú
    1. Sumar dos números
    2. Restar dos números
    3. Multiplicar dos números
    4. Dividir dos números
    5. Salir
    ''')
    n = int(input("Ingrese una opción: "))
    if n == 1:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print(f"La suma entre {a} y {b} es ", a + b)
    elif n == 2:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print(f"La resta entre {a} y {b} es {a - b}")
    elif n == 3:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print(f"La multiplicación entre {a} y {b} es {a * b}")
    elif n == 4:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print(f"La división entre {a} y {b} es {a / b}")
    elif n == 5:
        sw = False
    else:
        print(f'La opción {n} no esta disponible...')
    time.sleep(3)