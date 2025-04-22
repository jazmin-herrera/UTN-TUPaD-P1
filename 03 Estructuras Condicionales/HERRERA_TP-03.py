#Ejercicio 1
edad_minima = 18

edad = int(input ("Ingrese su edad: "))
if edad > edad_minima: 
    print("es mayor de edad")

#Ejercicio 2
nota_minima = 6
int(nota_minima)
nota = int(input("Ingrese su nota: "))
if nota >= nota_minima:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero:"))
if numero % 2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5
 contrasena = int(input("Ingrese contrasena: "))
 if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contrasena correcta")
else:
    print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, median, mean, StatisticsError

# Generar lista aleatoria
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Mostrar la lista
print("Lista de números aleatorios:", numeros_aleatorios)

# Calcular estadísticas
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    moda = "No hay una única moda"

# Mostrar resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinar el sesgo
if isinstance(moda, (int, float)):
    if media > mediana > moda:
        print("Sesgo positivo (a la derecha).")
    elif media < mediana < moda:
        print("Sesgo negativo (a la izquierda).")
    elif media == mediana == moda:
        print("Sin sesgo.")
    else:
        print("No se puede determinar el sesgo con claridad.")
else:
    print("No se puede determinar el sesgo porque no hay una única moda.")
#Ejercicio 7
# Solicitar frase
frase = input("Ingrese una frase o palabra: ")

# Verificar la última letra
if frase and frase[-1].lower() in 'aeiou':
    frase += "!"
    
print("Resultado:", frase)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("¿Cómo desea ver su nombre?")
print("1. Todo en mayúsculas")
print("2. Todo en minúsculas")
print("3. Solo la primera letra en mayúscula")

opcion = input("Elija 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida.")

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#Ejercico 10
# Datos del usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ")
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Convertir a formato día-mes
fecha = (mes, dia)

# Definir rangos de fechas
invierno = [((12, 21), (3, 20))]
primavera = [((3, 21), (6, 20))]
verano = [((6, 21), (9, 20))]
otonio = [((9, 21), (12, 20))]

def en_rango(fecha, inicio, fin):
    return (fecha >= inicio or fecha <= fin) if inicio > fin else (inicio <= fecha <= fin)

# Determinar estación
estacion = "desconocida"

for est, rango in zip(["invierno", "primavera", "verano", "otoño"], [invierno, primavera, verano, otonio]):
    for ini, fin in rango:
        if en_rango(fecha, ini, fin):
            estacion = est
            break

# Ajustar según hemisferio
if estacion == "desconocida":
    print("Fecha no válida.")
else:
    if hemisferio == "S":
        estaciones = {
            "invierno": "verano",
            "primavera": "otoño",
            "verano": "invierno",
            "otoño": "primavera"
        }
        estacion = estaciones[estacion]

    print(f"La estación es: {estacion.capitalize()}")

