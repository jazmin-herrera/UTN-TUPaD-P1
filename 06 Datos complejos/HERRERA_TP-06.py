#EJERCICIO 1
# # Creamos el diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Imprimimos el diccionario original
print(precios_frutas)

# Agregamos las frutas nuevas
# se añadirán las keys que no existen en el diccionario
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Imprimimos nueva versión del diccionario
print(precios_frutas)

####################################################################################

#EJERCICIO 2
# Modificamos los precios de las frutas
# Como estas keys ya existen en el diccionario, se modificarán
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Imprimimos nueva versión del diccionario
print(precios_frutas)

########################################################################

#EJERCICIO 3

frutas = precios_frutas.keys()

# Imprimimos el resultado
print(frutas)

frutas = list(frutas)

print(frutas)

###################################################################################

#EJERCICIO 4
contactos = {}

for _ in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre del contacto a consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Contacto no encontrado.")

#######################################################################

#EJERCICIO 5
frase = input("Ingresá una frase: ")
palabras = frase.split()

unicas = set(palabras)
print("Palabras únicas:", unicas)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento:", recuento)

##############################################################

#EJERCICIO 6
alumnos = {}

for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingresá la nota {i+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

#########################################################################

#EJERCICIO 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#EJERCICIO 8
productos = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}

producto = input("Ingresá el nombre del producto: ")

if producto in productos:
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá el stock inicial: "))
    productos[producto] = nuevo_stock
    print(f"Producto {producto} agregado con {nuevo_stock} unidades.")

############################################################################

#EJERCICIO 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividades programadas.")

######################################################

#EJERCICIO 10
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}

invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

print("Diccionario original:", paises)
print("Diccionario invertido:", invertido)
