# Ejercicio 1
print("hola mundo!")

# ejercicio 2
nombre = input ("ingrese su nombre: ")
print(f"hola ¨{nombre}")

#ejercicio 3
nombre1 = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
lugar = input("ingrese donde vive: ")
print(f"soy {nombre1} {apellido},tengo {edad} años y vivo en {lugar}")

# ejercicio 4
pi= 3.4
radio = int(input("ingrese radio de un circulo: "))
area = pi * radio * radio
perimetro = pi * 2 * radio
print(f"el area del circulo es: {area}")
print(f"el perimetro de un circulo es: {perimetro}")

# ejercicio 5
seg = int(input("ingrese cantidad de segundos: "))
hora = seg // 3600
print(f"la cantidad de horas son: {hora}")

# ejercicio 6
numero = int(input("ingrese un numero: "))
print(numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero *7, numero * 8, numero * 9, numero * 10)

# ejercicio 7
num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))
print(num1 + num2, num1 / num2, num1 * num2, num1 - num2)

# ejrcicio 8
alt = int(input("ingrese altura en metros: "))
pes = int(input("ingrese peso: "))
imc = pes / alt ** 2
print(f"ingrese la masa corporal es: {imc}")

# ejercicio 9
t = int(input("ingrese temperatura en grado celcius: "))
f = 9/5 * {t} + 32
print(f"su equivalente en grado fahrenheit: {f}")

# ejercicio 10
a = int(input("ingrese el primer numero:"))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero:"))
promedio =(a + b + c) / 3
print(f"El promedio de los tres números es: {promedio}")