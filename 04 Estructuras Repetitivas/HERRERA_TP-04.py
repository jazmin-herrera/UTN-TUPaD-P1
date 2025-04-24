#Ejercicio 1
for i in range(101):
    print(i)

###############################
#Ejercicio 2
int(input("Ingrese numero entero: "))

###############################

#Ejercicio 3
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print(f"La suma entre {inicio} y {fin} es: {suma}")

###############################

#Ejercicio 4
suma = 0
numero = int(input("Ingresa un número (0 para salir): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para salir): "))

print(f"Suma total: {suma}")

###############################

#Ejercicio 5
import random

secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == secreto:
        adivinado = True

print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")

###############################

#Ejercicio 6
for i in range(100, -1, -2):
    print(i)
###############################

#Ejercicio 7
n = int(input("Ingresa un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print(f"La suma de los números entre 0 y {n} es: {suma}")

###############################

#Ejercicio 8
pares = impares = positivos = negativos = 0

for _ in range(100):  # Cambia a menos para probar más fácil
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

###############################

#Ejercicio 9
suma = 0

for _ in range(100):  # Puedes usar 10 para probar
    numero = int(input("Ingresa un número: "))
    suma += numero

media = suma / 100
print(f"La media es: {media}")

###############################

#Ejercicio 10
numero = int(input("Ingresa un número: "))
numero_abs = abs(numero)
invertido = 0

while numero_abs > 0:
    digito = numero_abs % 10
    invertido = invertido * 10 + digito
    numero_abs //= 10

if numero < 0:
    invertido = -invertido

print(f"Número invertido: {invertido}")

