#Ejercicio 1
lista = list(range(1,101,4))
print(lista)
############################################################

#Ejercicio 2
lista_gustos = ["hamburguesa", "sushi", "helado", "tacos", "paella"]
print("El penultimo elemento es: ", lista_gustos [-3])

############################################################

#Ejercicio 3

lista_vacia = []
lista_vacia.append = ("Basquet")
lista_vacia.append = ("Futbol")
lista_vacia.append = ("Voley")
print("lista resultante: ", lista_vacia) 

##############################################################

#Ejercicio 4

animales = ["perro", "gato", "conejo","pez"]
animales [1] = "loro"
animales [-1] = "oso"
print("lista resultante:", animales)

##############################################################

#Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

Primero se crea una lista de números, que nos damos cuenta que hablamos de una lista porque esta entre corchetes. Luego indica que se
quiere eliminar un número, por lo tanto nombra la variable números seguido de un punto con la palabra remove (utilizada para eliminar 
un elemnto de lista), pero en este caso pide eliminar el número más grande de aquella lista, por eso coloca max(numeros).Finalmente pide
que se imprima por pantalla la lista actualizada, la cual sera [8, 15, 3, 7], ya que el número más grande de esta lista era el 22.


##############################################################

#Ejercicio 6
lista = list(range(10,31,5))
print("los dosprimeros numeros son: ", numeros [0] y numeros [1])

##############################################################

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos [1] = "peugeot"
autos [2] = "ford"

#################################################################

#Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#################################################################

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append = ("jugo")

compras[1][1] = "tallarines"

compras[0].remove = ("pan")

print(compras)

##################################################################

#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
