# Programa 1 mascotas 
# Fecha: 2024/10/28
# Elaborado por: Jazmin Macias Sabas 
mascota = input("Ingresa el tipo de mascota: ")
if "perro" in mascota:
    print("Es un perro")
elif "gato" in mascota:
    print("Tienes un gato")
else: 
    print("Tipo de mascota desconocida")
    print("Gracias por usar nuestro programa")

# Programa 2 Programa que Indique si, de dos enteros ingresados, el primero es mayor, igual o menor que el segundo 
# Fecha: 2024/10/28
# Elaborado por: Jazmin Macias Sabas 
n1 = int(input("ingresa el numero 1: "))
n2 = int(input("ingresa el numero 2: "))
if n1 > n2:
    print ("El numero " + str(n1) + " es mayor al " + str (n2))
elif n1 == n2:
    print("Son números iguales")
else:
    print("El numero " + str (n1) + " es menor al número " + str(n2) 

# Programa 3 Identificación de tipos de datos str, int y float 
# Fecha: 2024/10/28
# Elaborado por: Jazmin Macias Sabas 
variable = input("Ingresa tu edad: ")
print(type(variable))

variable = int(variable) #Convertir la variable a tipo entero 
print(type(variable))

variable = float(variable) #Convertir la variable a tipo flotante 
print(type(variable))

# Programa 4 Impuestos de un empleado
# Fecha: 2024/10/29
# Elaborado por: Jazmin Macias Saba 
def calcular_impuesto(ingreso):
    if ingreso <= 1000:
        impuesto = ingreso * 0.05
    elif ingreso >1000 and ingreso <= 2500:
        impuesto = ingreso * 0.08 
    elif ingreso >2500 and ingreso < 6000:
        impuesto = ingreso * 0.12
    elif ingreso >= 6000:
        impuesto = ingreso * 0.15
    else:
        impuesto = (1000 * 0.05) + (2500 * 0.08) + (2501 * 0.12) + (6000 * 0.15)
    
    return impuesto

# Solicitar el ingreso al usuario
ingreso_empleado = float(input("¿Cuales son tus ingresos?: "))
impuesto_a_pagar = calcular_impuesto(ingreso_empleado)

# Calcular el salario final
salario_final = ingreso_empleado - impuesto_a_pagar

# Mostrar resultados
print(f"Tus impuestos son: ${impuesto_a_pagar:.2f}")
print(f"Tu salario final es: ${salario_final:.2f}")

# Programa 5 Nivel de desempeño de un estudiante 
# Fecha: 2024/10/29
# Elaborado por: Jazmin Macias Saba 
# Solicitar la calificación al usuario
calificación = float(input("Calificación del estudiante (0-100): "))

# Determinar el nivel de desempeño
if calificacion <= 60:
    desempeño = "Insuficiente"
elif 60 < calificación <= 79 :
    desempeño = "Suficiente"
elif 79 < calificación <= 89:
    desempeño = "Muy bien"
elif 89 < calificación <= 95:
    desempeño = "Notable"
elif 95 < calificación <= 100:
    desempeño = "Excelente"

# Mostrar el resultado
print(f"El nivel de desempeño es: {desempeno}")

# Programa 6 Listas 
# Fecha: 2024/10/30
# Elaborado por: Jazmin Macias Sabas 
print("Lista de enteros")
print(["5, 8, 10"])

print("\nLista de textos")
print(["Manzana", "Piña", "Naranja"])

print("\nLista de booleanos")
print(["True, False, True"])

print(("\nLista vacía"))
print([])

# Programa 7 Tipos de datos Lista y tipos de datos de los elementos 
# Fecha: 2024/10/30
# Elaborado por: Jazmin Macias Sabas 
cadenas = ["Juan", "Pedro", "Chuy"]
print(cadenas)
print(cadenas[1])
print(type(cadenas))
print(type(cadenas[1]))

# Programa 8 Operaciones con listas
# Fecha: 2024/10/30
# Elaborado por: Jazmin Macias Sabas 
print("Indexing")
numeros = [10, 20, 30]
print(numeros[2])
print(numeros[0])
print(numeros[1])
print(numeros[-1])
print("\nSubscripting")
nombres = ["Chorchis", "Choto", "Emiliano", "Pepe el toro"]
print(nombres[1:])
print(nombres[1:5])
print(nombres[-2:])

# Programa 9 Compare puntos con todas las demás listas 
# Fecha: 2024/10/31
# Elaborado por: Jazmin Macias Sabas
puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_texto = ["10", "20", "30"]
print(puntos==puntos_2) #True
print(puntos==ordenados) #False
print(puntos==puntos_texto) #False
print(puntos!=puntos_2) #False
print(puntos!=ordenados) #True 
print(puntos!=puntos_texto) #True 

# Programa 10 List Membership
# Fecha: 2024/10/31
# Elaborado por: Jazmin Macias Sabas
nombres = ["Choto", "Emilio", "Luis"]
print("Luis" in nombres) #True
print("Emi" in nombres) #False
print("Javier" in nombres) #False
print("Jose" not in nombres) #True

# Programa 11 Agregar elementos a una lista
# Fecha: 2024/10/31
# Elaborado por: Jazmin Macias Sabas
colores = ["rojo", "azul"]
print(colores)
colores.append("verde")
print(colores)

# Programa 12 Método pop
# Fecha: 2024/10/31
# Elaborado por: Jazmin Macias Sabas
# Creamos una lista 
mi_lista = ["Rojo", "Verde", "Morado", "Azul", "Naranja"]

# Usamos pop para eliminar y devolver el último elemento
ultimo_elemento = mi_lista.pop()
print("Elemento eliminado:", ultimo_elemento)
print("Lista después de usar pop:", mi_lista)

# Usamos pop para eliminar y devolver el elemento en la posición 1
elemento_en_posicion_1 = mi_lista.pop(1)
print("Elemento eliminado en la posición 1:", elemento_en_posicion_1)
print("Lista después de usar pop en la posición 1:", mi_lista)

# Programa 1 ciclos "for"
# Fecha: 2024/11/04
# Elaborado por: Jazmin Macias Sabas
lista_num = [10, 30, 40, 20, 35, 80]
print(lista_num [0])
print(lista_num [1])
print(lista_num [2])
print(lista_num [3])
print(lista_num [4])
print(lista_num [5])
# Haciendo lo mismo pero con un ciclo "for"
for i in lista_num:
    print(i)

# Programa 2 programa que imprima los nombres 
# Fecha: 2024/11/04
# Elaborado por: Jazmin Macias Sabas
nombres = ["Luis", "Chuy", "Mauricio"]
for nombre in nombres: 
    print("El nombre es: ",nombre)

# Programa 3 Función rango 
# Fecha: 2024/11/04
# Elaborado por: Jazmin Macias Sabas
print("Imprime los valores del 0 al 9:")
x = range (10)
for num in x:
    print(num)

print("Imprime los valores del 5 al 15:")
x1 = range (5,16)
for num in x1:
    print(num)

print("\nImprime los pares del 10 al 20:")
x2 = range (10, 21, 2)
for num in x2:
    print(num)
    
print("\nImprime los impares del 11 al 21:")
x3 = range (11, 22, 2)
for num in x3:
    print(num)

#Programa.4 Programa que imprima el nombre de mis 10 personajes favoritos
# Fecha: 2024/11/04
# Elaborado por: Jazmin Macias Sabas 


personajes = ["Nick","spiderman","Loki","Flynn Rider","Adam Carlsen","Venom","Alexander","Hades","El genio de la lámpara","Patrick Verona"]

# Imprimir cada personaje en la lista
print("Mis 10 personajes favoritos son:")
for personajes in personajes:
    print(personajes)

print("Gracias por ver mis 10 personajes favoritos")

# Programa 5 
# Fecha: 2024/11/05
# Elaborado por: Jazmin Macias Sabas
letras = ["a","b","c","d","e"]
contador = 0 #inicializa variable 
for letra in letras:
    contador = contador +1 
print("La lista \"letras\" tiene",contador,"letras")
números = [100,200,300,400]
sumatoria = 0 # inicialización 
for número in números:
    sumatoria = sumatoria + número
print("La sumatoria es", sumatoria)
palabras = ["Hoy"," ","hace"," ","frío"]
mensaje = ""
for palabra in palabras:
    mensaje = mensaje + palabra
print(mensaje)
lista_anterior = ["Manzana","Piña","Uva"]
lista_nueva = []
print("La lista vacia", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
print("La lista copiada es:", lista_nueva)

# Programa 6 Números menores a 50 
# Fecha: 2024/11/06
# Elaborado por: Jazmin Macias Sabas
numeros = [10,50,25,13,10,28,100,500,29,29]
menores_50 = []
for numero in numeros:
    if numero < 50:
        menores_50.append(numero)
print("La lista original es: ",numeros)
print("La nueva lista es: ",menores_50)

# Programa 7 Programa que clasifica las edades de una lista menores de 18, entre 18 y 65 y mayores de 65 el programa debe imprimir cuales edades hay en cada grupo 
# Fecha: 2024/11/07
# Elaborado por: Jazmin Macias Sabas
edades = [10,15,18,8, 36,25,67,89,95,43,26,10,65,55,81,90,64]
menores_18 = [] # Lista vacía para menores de 18 
adultos = []    # lista vacía para adultos entre 18 y 65 
mayores_65 = [] # Lista vacía para mayores de 65 

for edad in edades:
    if edad < 18:
        menores_18.append(edad)
    elif edad >= 18 and edad <= 65:
        adultos.append(edad)
    else:
        mayores_65.append(edad)
        
print("\nLa lista de edades es: ",edades)
print("\nLa lista de menores es: ",menores_18)
print("\nLa lista de adultos es: ",adultos)
print("\nLa lista de adultos mayores es: ",mayores_65)

# Programa 8
# Fecha: 2024/11/07
# Elaborado por: Jazmin Macias Sabas

# Ejemplo 1 
# Imprimir los numeros del 1 al 10 
i = 1 #Inicializacion de la variable de control 
while i <= 10: # Condicion de parada
    print(i)
    i += 1 # Equivalente a i = i + 1 
# Sintaxis:
# while <condicional>:
# <cuerpo del while>

# Ejemplo 2 
# Imprimir los numeros del 10 al 1 
i = 10
while i >= 1:
    print(i)
    i -= 1 

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1 # Equivalente a i = i + 1 
print("Fin del programa")

# Ejemplo 2 - continue 
# Imprimir los números del 1 al 10, pero si el número es 5 evitarlo 
i = 1 
while i <= 10 :
    if i == 5:
        i += 1
        continue 
    print(i)
    i += 1
print("Fin del programa")

# Programa 10 Programa para demostrar el funcionamiento de los métodos upper y lower 
# Fecha: 2024/11/08
# Elaborado por: Jazmin Macias Sabas

#Definimos una cadena de texto 
cadena = "Python es un lenguaje de programación"
print("\n",cadena)

cadena_mayusculas = cadena.upper()  # Convertimos la cadena a mayúsculas
print("\n" ,cadena_mayusculas)

cadena_minusculas = cadena.lower() # Convertimos la cadena a mayúsculas
print("\n" , cadena_minusculas)
print("\n Fin del programa")

# Programa 11 Programa que se repite hasta que ingrese la palabra salir 
# Fecha: 2024/11/08
# Elaborado por: Jazmin Macias Sabas

# Iniciación de variables 
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o salir para terminar: ")
    palabra = palabra.lower() # Convierte la palabra a minúscula
    print("Usted ingreso:", palabra)
print("Fin del programa")

# Programa 12 
# Fecha: 2024/11/08
# Elaborado por: Jazmin Macias Sabas

# Inicialización de variables
palabra = ""
while True:
    palabra = input("ingresa una palabra o salir para terminar: ")
    palabra = palabra.lower() # Convertir la palabra a minúsculas
    print("Usted ingreso: ", palabra)
    if palabra == "salir":
        break

print("Fin del programa \U0001F601 \n\n") # Imprime un emoji feliz 
print("¡Hasta luego! \U0001F44B \n") # Imprime un emoji de saludo



