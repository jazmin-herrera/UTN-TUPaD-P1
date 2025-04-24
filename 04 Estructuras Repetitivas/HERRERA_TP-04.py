#Ejercicio 1
for i in range(101):
    print(i)

###############################
#Ejercicio 2
umero = int(input("Ingresa un número entero: "))  
cantidad_digitos = len(str(abs(numero)))  
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

###############################

#Ejercicio 3
valor1 = int(input("Ingresa el primer valor entero: "))
valor2 = int(input("Ingresa el segundo valor entero: "))

if valor1 < valor2:
    inicio = valor1 + 1
    fin = valor2
else:
    inicio = valor2 + 1
    fin = valor1

suma = 0
for numero in range(inicio, fin):
    suma += numero
suma = sum(range(inicio, fin))

print(f"La suma de los números entre {valor1} y {valor2}, excluyéndolos, es: {suma}")

###############################

#Ejercicio 4
total = 0

print("Ingresa números enteros para sumarlos. Ingresa 0 para finalizar.")

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:  
        break
    total += numero  

print(f"El total acumulado es: {total}")

###############################

#Ejercicio 5
import random

numero_secreto = random.randint(0, 9)

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 0 y 9. ¿Puedes adivinar cuál es?")

intentos = 0  
acertado = False  


while not acertado:
    
    intento = int(input("Ingresa tu intento: "))
    intentos += 1  

    
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        acertado = True  
    elif intento < numero_secreto:
        print("El número es mayor. ¡Inténtalo de nuevo!)
    else:
        print("El número es menor. ¡Inténtalo de nuevo!")  


print(f"Lo lograste en {intentos} intentos. ¡Buen trabajo!")

###############################

#Ejercicio 6
for i in range(100, -1, -2):
    print(i)
###############################

#Ejercicio 7
if numero >= 0:
    suma = 0
    for i in range(numero + 1):  
        suma += i
    print(f"La suma de los números entre 0 y {numero} es: {suma}")
else:
    print("Por favor, ingresa un número entero positivo.")

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
cantidad_numeros = 100


suma = 0


print(f"Ingresa {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))  
    suma += numero  


media = suma / cantidad_numeros


print(f"\nLa media de los números ingresados es: {media}")

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

