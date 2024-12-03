 # Bloques-de-programa-3-y-4
Explicación de los programas 
```
Ejercicio 1 Equivalencia elif  else + if 
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
```
1. Almacena la mascota escrita por el usuario en la variable "mascota":
mascota = input("Ingresa el tipo de mascota: ")

2. Verifica si el valor de la variable "mascota" contiene la palabra "perro":
if "perro" in mascota:
    print("Es un perro")
Si la palabra "perro" está presente en la variable "mascota", se imprimirá "Es un perro" en la consola.

3. En caso de que la palabra "perro" no esté presente en la variable "mascota", se procede a verificar si la entrada contiene la palabra "gato" mediante la condición "elif":
elif "gato" in mascota:
    print("Tienes un gato")
Si la variable "mascota" contiene la palabra "gato", se imprimirá "Tienes un gato" en la consola.

4. Si ninguna de las condiciones anteriores se cumple, se llega a la condición "else". Esta condición indica que ninguna de las palabras buscadas ("perro" o "gato") está presente en la variable "mascota":
else: 
    print("Tipo de mascota desconocida")
    print("Gracias por usar nuestro programa")
En este caso, se imprimirán los mensajes "Tipo de mascota desconocida" y "Gracias por usar nuestro programa" en la consola.

```
Ejercicio 2 Indica si, de dos enteros ingresados, el primero es mayor, igual o menor que el segundo
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
```
1. Se solicitan al usuario que ingrese dos números enteros. Las entradas se almacenan en las variables "n1" y "n2", respectivamente. El uso de la función "int()" garantiza que la entrada se convierta en un número entero:
n1 = int(input("ingresa el numero 1: "))
n2 = int(input("ingresa el numero 2: "))

2. Se utiliza una condición "if" para verificar si el valor de "n1" es mayor que el de "n2":
if n1 > n2:
    print ("El numero " + str(n1) + " es mayor al " + str (n2))
Si la condición se cumple, se imprimirá un mensaje en la consola indicando que el primer número ingresado es mayor que el segundo número.

3. En caso de que la condición "if" no se cumpla, el programa continúa con la condición "elif" para verificar si los valores de "n1" y "n2" son iguales:
elif n1 == n2:
    print("Son números iguales")
Si la condición "elif" se cumple, se imprimirá un mensaje en la consola indicando que los números ingresados son iguales.

4. Si ninguna de las condiciones anteriores se cumple, se concluye que el valor de "n1" es menor que el de "n2". En este caso, se ejecuta la condición "else" y se imprime un mensaje en la consola indicando que el primer número es menor que el segundo:
else:
    print("El numero " + str (n1) + " es menor al número " + str(n2))

```
Ejercicio 3 Identificación de tipos de datos 
# Identificación de tipos de datos str, int y float 
# Fecha: 2024/10/28
# Elaborado por: Jazmin Macias Sabas 
variable = input("Ingresa tu edad: ")
print(type(variable))

variable = int(variable) #Convertir la variable a tipo entero 
print(type(variable))

variable = float(variable) #Convertir la variable a tipo flotante 
print(type(variable))
```
1. Se solicita al usuario que ingrese su edad, y se almacena la entrada en la variable "variable":
variable = input("Ingresa tu edad: ")
En Python, la función input() siempre devuelve una cadena de texto (str), sin importar si la entrada consiste en números o letras.

2. Se imprime el tipo de dato de la variable "variable" utilizando la función "type()":
print(type(variable))
Esto imprimirá <class 'str'> en la consola, ya que la entrada del usuario se almacena como una cadena de texto (str).

3. Se convierte la entrada del usuario a un número entero (int) y se almacena en la misma variable "variable":
variable = int(variable) #Convertir la variable a tipo entero
Esto convertirá la entrada del usuario en un número entero, siempre y cuando la entrada sea una cadena de texto numérica válida.

4. Se imprime nuevamente el tipo de dato de la variable "variable":
print(type(variable))
Ahora se imprimirá <class 'int'> en la consola, debido a que la variable ha sido convertida a un entero.

5. Se convierte la variable "variable" a un número flotante (float):
variable = float(variable) #Convertir la variable a tipo flotante

6. Se imprime nuevamente el tipo de dato de la variable "variable":
print(type(variable))
Esta vez, se imprimirá <class 'float'> en la consola, ya que la variable ha sido convertida a un número flotante.

```
Ejercicio 4 Programa que calcule los impuestos que debe pagar un empleado de acuerdo con la siguiente tabla  
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
```
1. Se define una función que toma un argumento, el ingreso de un empleado:
def calcular_impuesto(ingreso):

2. Se definen las condiciones para calcular el impuesto según la tabla. Si el ingreso es menor o igual a 1000, se aplica un 5% de impuesto:
    if ingreso <= 1000:
        impuesto = ingreso * 0.05

3. Si el ingreso está entre 1001 y 2500, se aplica un 8% de impuesto:
    elif ingreso >1000 and ingreso <= 2500:
        impuesto = ingreso * 0.08


4. Si el ingreso está entre 2501 y 6000, se aplica un 12% de impuesto:
    elif ingreso >2500 and ingreso < 6000:
        impuesto = ingreso * 0.12

5. Si el ingreso es mayor o igual a 6000, se aplica un 15% de impuesto:
    elif ingreso >= 6000:
        impuesto = ingreso * 0.15

6. En caso de que el ingreso no se ajuste a las condiciones anteriores, se calcula el impuesto usando todos los rangos de impuestos:
    else:
        impuesto = (1000 * 0.05) + (2500 * 0.08) + (2501 * 0.12) + (6000 * 0.15)

7. La función devuelve el cálculo del impuesto:
    return impuesto
Luego, se solicita al usuario que ingrese su ingreso, se llama a la función para calcular el impuesto y se calcula el salario final restando el impuesto del ingreso. Finalmente, se muestran los resultados en pantalla:

Solicitar el ingreso al usuario
ingreso_empleado = float(input("¿Cuales son tus ingresos?: "))
impuesto_a_pagar = calcular_impuesto(ingreso_empleado)

Calcular el salario final
salario_final = ingreso_empleado - impuesto_a_pagar

Mostrar resultados
print(f"Tus impuestos son: ${impuesto_a_pagar:.2f}")
print(f"Tu salario final es: ${salario_final:.2f}")

Este programa te permite calcular el impuesto y el salario final de un empleado según su ingreso y una tabla de impuestos pre-establecida.

```
Ejercicio 5 Programa que calcule el nivel de desempeño de un estudiante respecto a su calificación dada por el usuario de acuerdo con la siguiente tabla  
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
```
1. Se solicita al usuario que ingrese la calificación del estudiante, la cual se almacena en la variable "calificación":
calificación = float(input("Calificación del estudiante (0-100): "))

2. Se define una variable "desempeño" que almacenará el nivel de desempeño del estudiante. Se utiliza una estructura de control "if-elif-else" para evaluar la calificación:
if calificacion <= 60:
    desempeño = "Insuficiente"
Si la calificación es menor o igual a 60, se asigna el valor "Insuficiente" a la variable "desempeño".

elif 60 < calificación <= 79 :
    desempeño = "Suficiente"
Si la calificación está entre 60 y 79 (ambos inclusive), se asigna el valor "Suficiente" a la variable "desempeño".

elif 79 < calificación <= 89:
    desempeño = "Muy bien"
Si la calificación está entre 79 y 89 (ambos inclusive), se asigna el valor "Muy bien" a la variable "desempeño".

elif 89 < calificación <= 95:
    desempeño = "Notable"
Si la calificación está entre 89 y 95 (ambos inclusive), se asigna el valor "Notable" a la variable "desempeño".

elif 95 < calificación <= 100:
    desempeño = "Excelente"
Si la calificación está entre 95 y 100 (ambos inclusive), se asigna el valor "Excelente" a la variable "desempeño".

3. Se imprime el nivel de desempeño del estudiante:
print(f"El nivel de desempeño es: {desempeño}")

Este programa permite determinar el nivel de desempeño de un estudiante en función de su calificación ingresada por el usuario, asignando un nivel de desempeño predefinido en función de los rangos de calificaciones determinados.

```
Ejercicio 6 Programa de listas 
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
```
1. Se crea una lista de enteros y se imprime:
print("Lista de enteros")
print(["5, 8, 10"])
La lista contiene las cadenas "5", "8" y "10" separadas por comas y entre corchetes. Al imprimirla, se mostrarán los elementos de la lista entre corchetes y separados por comas.

2. Se crea una lista de textos (strings) y se imprime:
print("\nLista de textos")
print(["Manzana", "Piña", "Naranja"])
Esta lista contiene las cadenas "Manzana", "Piña" y "Naranja" separadas por comas y entre corchetes. Al imprimirla, se mostrarán los elementos de la lista entre corchetes y separados por comas.

3. Se crea una lista de booleanos y se imprime:
print("\nLista de booleanos")
print(["True, False, True"])
En este caso, la lista contiene las cadenas "True", "False" y "True", separadas por comas y entre corchetes. Al imprimirla, se mostrarán los elementos de la lista entre corchetes y separados por comas.

4. Se crea una lista vacía y se imprime:
print(("\nLista vacía"))
print([])
Al imprimir esta lista vacía, se mostrará [] en la consola.

Este programa ilustra la creación y la impresión de listas en Python, con diferentes tipos de datos y longitudes, incluyendo listas vacías.

```
Ejercicio 7 Tipos de datos en las listas 
# Programa 7 Tipos de datos Lista y tipos de datos de los elementos 
# Fecha: 2024/10/30
# Elaborado por: Jazmin Macias Sabas 
cadenas = ["Juan", "Pedro", "Chuy"]
print(cadenas)
print(cadenas[1])
print(type(cadenas))
print(type(cadenas[1]))
```
1. Se crea una lista llamada "cadenas" con tres elementos de tipo string:
cadenas = ["Juan", "Pedro", "Chuy"]

2. Se imprime la lista completa:
print(cadenas)
Al imprimir la lista, se mostrarán todos los elementos entre corchetes y separados por comas: ['Juan', 'Pedro', 'Chuy'].

3. Se imprime el segundo elemento de la lista (Pedro) accediendo al índice 1 de la lista:
print(cadenas[1])
El resultado será Pedro.

4. Se imprime el tipo de dato de la lista utilizando la función type():
print(type(cadenas))
El tipo de dato de la lista es <class 'list'>, lo que significa que es una lista en Python.

5. Se imprime el tipo de dato del segundo elemento de la lista (Pedro) utilizando la función type():
print(type(cadenas[1]))
El tipo de dato del segundo elemento es <class 'str'>, lo que significa que es una cadena de texto (string) en Python.

Este programa ilustra cómo crear una lista con elementos de un tipo de dato determinado (en este caso, strings) y cómo determinar el tipo de dato de la lista y de sus elementos utilizando la función type().

```
Ejercicio 8 Operaciones con listas 
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
```
1. Se imprime el encabezado "Indexing":
print("Indexing")

2. Se crea una lista de números y se imprimen elementos específicos utilizando indexación:
numeros = [10, 20, 30]
print(numeros[2])  # Imprime el tercer elemento (índice 2)
print(numeros[0])  # Imprime el primer elemento (índice 0)
print(numeros[1])  # Imprime el segundo elemento (índice 1)
print(numeros[-1]) # Imprime el último elemento (índice -1)

La salida será:

30
10
20
30

3. Se imprime el encabezado "Subscripting":
print("\nSubscripting")

4. Se crea una lista de nombres y se imprimen segmentos de la lista usando segmentación:
nombres = ["Chorchis", "Choto", "Emiliano", "Pepe el toro"]
print(nombres[1:]) # Imprime desde el segundo elemento hasta el final
print(nombres[1:5]) # Imprime desde el segundo elemento hasta el índice 5 (no incluido)
print(nombres[-2:]) # Imprime los dos últimos elementos

La salida será:
['Choto', 'Emiliano', 'Pepe el toro']
['Choto', 'Emiliano']
['Emiliano', 'Pepe el toro']

Este programa demuestra cómo acceder a elementos individuales de una lista utilizando indexación y cómo obtener segmentos de la lista utilizando segmentación.

```
Ejercicio 9 Igualdad en listas 
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
```
1. Se crean cuatro listas diferentes: "puntos", "puntos\_2", "ordenados", y "puntos\_texto". Las listas "puntos" y "puntos\_2" tienen el mismo contenido pero diferente en la variable en la que se almacena. La lista "ordenados" tiene los mismos números pero en orden ascendente. La lista "puntos\_texto" contiene las cadenas de texto de los números presentes en las otras listas:
puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_texto = ["10", "20", "30"]

2. Se imprime la comparación de igualdad entre las listas "puntos" y "puntos\_2" usando el operador ==:
print(puntos==puntos_2) #True
El resultado será True ya que las listas son idénticas en contenido y orden.

3. Se imprime la comparación de igualdad entre las listas "puntos" y "ordenados" usando el operador ==:
print(puntos==ordenados) #False
El resultado será False ya que, aunque tienen los mismos elementos, las listas tienen diferente orden.

4. Se imprime la comparación de igualdad entre las listas "puntos" y "puntos\_texto" usando el operador ==:
print(puntos==puntos_texto) #False
El resultado será False ya que las listas tienen contenido diferente: una contiene enteros y la otra contiene strings (cadenas de texto).

5. Se imprime la comparación de desigualdad entre las listas "puntos" y "puntos\_2" usando el operador !=:
print(puntos!=puntos_2) #False
El resultado será False ya que las listas son idénticas en contenido y orden.

6. Se imprime la comparación de desigualdad entre las listas "puntos" y "ordenados" usando el operador !=:
print(puntos!=ordenados) #True
El resultado será True ya que las listas tienen diferente orden.

7. Se imprime la comparación de desigualdad entre las listas "puntos" y "puntos\_texto" usando el operador !=:
print(puntos!=puntos_texto) #True
El resultado será True ya que las listas tienen contenido diferente: una contiene enteros y la otra contiene strings (cadenas de texto).

Este programa muestra cómo evaluar la igualdad y desigualdad entre listas en Python y cómo se toman en cuenta el contenido, el orden y los tipos de datos de los elementos en la comparación.

```
Ejercicio 10 List Membership 
# Programa 10 List Membership
# Fecha: 2024/10/31
# Elaborado por: Jazmin Macias Sabas
nombres = ["Choto", "Emilio", "Luis"]
print("Luis" in nombres) #True
print("Emi" in nombres) #False
print("Javier" in nombres) #False
print("Jose" not in nombres) #True
```
1. Se crea una lista llamada "nombres" que contiene tres elementos:
nombres = ["Choto", "Emilio", "Luis"]

2. Se imprime la verificación de la membresía del elemento "Luis" en la lista "nombres" usando el operador in:
print("Luis" in nombres) #True
El resultado será True ya que el elemento "Luis" se encuentra en la lista.

3. Se imprime la verificación de la membresía del elemento "Emi" en la lista "nombres" usando el operador in:
print("Emi" in nombres) #False
El resultado será False ya que el elemento "Emi" no se encuentra en la lista.

4. Se imprime la verificación de la membresía del elemento "Javier" en la lista "nombres" usando el operador in:
print("Javier" in nombres) #False
El resultado será False ya que el elemento "Javier" no se encuentra en la lista.

5. Se imprime la verificación de la membresía del elemento "Jose" en la lista "nombres" usando el operador not in:
print("Jose" not in nombres) #True
El resultado será True ya que el elemento "Jose" no se encuentra en la lista.

Este programa ilustra cómo verificar la presencia o ausencia de elementos en una lista Python utilizando la membresía. Los operadores in y not in devolverán True o False en función de si el elemento se encuentra o no dentro de la lista, respectivamente.

```
Ejercicio 11 Agregar elementos a una lista 
# Programa 11 Agregar elementos a una lista
# Fecha: 2024/10/31
# Elaborado por: Jazmin Macias Sabas
colores = ["rojo", "azul"]
print(colores)
colores.append("verde")
print(colores)
```
1. Se crea una lista llamada "colores" con dos elementos:
colores = ["rojo", "azul"]


2. Se imprime la lista "colores":
print(colores)
La salida será ['rojo', 'azul'].

3. Se utiliza el método append() para agregar un nuevo elemento a la lista "colores":
colores.append("verde")
El método append() agrega el elemento "verde" al final de la lista.

4. Se imprime la lista "colores" luego de agregar el elemento "verde":
print(colores)
La salida será ['rojo', 'azul', 'verde'], demostrando que el elemento "verde" se ha agregado correctamente al final de la lista.

Este programa muestra cómo agregar un elemento a una lista en Python utilizando el método append(). Este método es útil cuando se desea agregar un nuevo elemento al final de una lista existente.

```
Ejercicio 12 programa utilizando el método pop () en una lista 
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
```
1. Se crea una lista llamada "mi\_lista" con cinco elementos:
mi_lista = ["Rojo", "Verde", "Morado", "Azul", "Naranja"]

2. Se utiliza el método pop() para eliminar y devolver el último elemento de la lista. Luego, se imprimen el elemento eliminado y la lista después de utilizar pop():
Usamos pop para eliminar y devolver el último elemento
ultimo_elemento = mi_lista.pop()
print("Elemento eliminado:", ultimo_elemento)
print("Lista después de usar pop:", mi_lista)

El resultado será:
yaml
Elemento eliminado: Naranja
Lista después de usar pop: ['Rojo', 'Verde', 'Morado', 'Azul']

3. Se utiliza el método pop() con el argumento 1 para eliminar y devolver el elemento en la posición 1 (índice 1) de la lista. Luego, se imprimen el elemento eliminado y la lista después de utilizar pop():
Usamos pop para eliminar y devolver el elemento en la posición 1
elemento_en_posicion_1 = mi_lista.pop(1)
print("Elemento eliminado en la posición 1:", elemento_en_posicion_1)
print("Lista después de usar pop en la posición 1:", mi_lista)

El resultado será:
yaml
Elemento eliminado en la posición 1: Verde
Lista después de usar pop en la posición 1: ['Rojo', 'Morado', 'Azul']

Este programa muestra cómo eliminar y devolver elementos de una lista en Python utilizando el método pop(). Puede eliminar tanto el último elemento (sin argumentos) como un elemento en una posición específica (con un argumento de índice).
```
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
```
1. Se crea una lista llamada "lista\_num" con seis elementos (10, 30, 40, 20, 35, y 80).
2. Las líneas con "print(lista\_num [índice])" imprimen el valor del elemento de la lista ubicado en el índice especificado (en este caso, del 0 al 5). Esto imprime cada elemento de la lista.
3. La línea "# Haciendo lo mismo pero con un ciclo "for"" es un comentario que indica que se mostrará otra forma de hacer lo mismo pero utilizando un bucle "for".
4. El bucle "for" recorre cada elemento en la lista "lista\_num". En cada iteración, la variable "i" toma el valor del siguiente elemento de la lista y luego se imprime.

Por lo tanto, el código imprime todos los elementos de la lista "lista\_num" dos veces: primero utilizando los índices de la lista, y luego con el bucle "for".

```
# Programa 2 programa que imprima los nombres 
# Fecha: 2024/11/04
# Elaborado por: Jazmin Macias Sabas
nombres = ["Luis", "Chuy", "Mauricio"]
for nombre in nombres: 
    print("El nombre es: ",nombre)
```
1. Se crea una lista llamada "nombres" que contiene tres nombres: "Luis", "Chuy", y "Mauricio".
2. El bucle "for" recorre cada elemento en la lista "nombres". En cada iteración, la variable "nombre" toma el valor del siguiente nombre en la lista.
3. Dentro del bucle "for", la línea "print("El nombre es: ",nombre)" imprime una frase que incluye el texto "El nombre es: " seguido del nombre actual en la variable "nombre".

El código imprime la frase "El nombre es: " seguida del nombre para cada elemento en la lista "nombres". En este caso, imprimirá lo siguiente:

text
El nombre es: Luis
El nombre es: Chuy
El nombre es: Mauricio

Esto muestra cómo puedes utilizar un bucle "for" para iterar sobre una lista y realizar una acción (como imprimir un mensaje personalizado) para cada elemento de la lista.

```
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
```
1. Impresión de valores del 0 al 9:
   print("Imprime los valores del 0 al 9:")
   x = range(10)
   for num in x:
       print(num)
   
   - range(10) genera una secuencia de números desde 0 hasta 9 (el 10 no se incluye).
   - El bucle for recorre cada número en esa secuencia y lo imprime.

2. Impresión de valores del 5 al 15:
   print("Imprime los valores del 5 al 15:")
   x1 = range(5, 16)
   for num in x1:
       print(num)
   
   - range(5, 16) genera una secuencia de números desde 5 hasta 15 (el 16 no se incluye).
   - Nuevamente, el bucle for recorre esos números e imprime cada uno.

3. Impresión de números pares del 10 al 20:
   python
   print("\nImprime los pares del 10 al 20:")
   x2 = range(10, 21, 2)
   for num in x2:
       print(num)
   
- range(10, 21, 2) genera una secuencia que comienza en 10 y termina en el número más cercano a 21 (sin incluirlo), con un incremento de 2. Esto significa que solo se imprimirán los números pares: 10, 12, 14, 16, 18 y 20.
   
4. Impresión de números impares del 11 al 21:
   python
   print("\nImprime los impares del 11 al 21:")
   x3 = range(11, 22, 2)
   for num in x3:
       print(num)
   
- range(11, 22, 2) genera una secuencia que comienza en 11 y termina en el número más cercano a 22 (sin incluirlo), con un incremento de 2. Esto imprimirá los números impares: 11, 13, 15, 17, 19 y 21.

En resumen, el código demuestra cómo usar la función range() para crear diferentes rangos de números y luego imprimirlos utilizando un bucle "for". ¡Es una forma muy eficiente de trabajar con secuencias numéricas

```
#Programa.4 Programa que imprima el nombre de mis 10 personajes favoritos
# Fecha: 2024/11/04
# Elaborado por: Jazmin Macias Sabas 


personajes = ["Nick","spiderman","Loki","Flynn Rider","Adam Carlsen","Venom","Alexander","Hades","El genio de la lámpara","Patrick Verona"]

# Imprimir cada personaje en la lista
print("Mis 10 personajes favoritos son:")
for personajes in personajes:
    print(personajes)

print("Gracias por ver mis 10 personajes favoritos")
```
1. Se define una lista llamada "personajes" con los nombres de tus diez personajes favoritos.
2. Se imprime un mensaje que dice "Mis 10 personajes favoritos son:" para presentar la lista.
3. El bucle "for" recorre cada elemento (en este caso, cada nombre) en la lista "personajes".
4. En cada iteración, la variable "personajes" toma el valor del siguiente nombre en la lista y se imprime.
5. Después de imprimir todos los nombres, se muestra un mensaje de agradecimiento: "Gracias por ver mis 10 personajes favoritos".

En resumen, el código crea una lista de tus diez personajes favoritos y luego utiliza un bucle "for" para imprimir cada nombre en la lista.

```
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
```
Bloque 1:
Este bloque recorre una lista de letras y cuenta la cantidad de elementos en la lista utilizando una variable llamada "contador". La variable se incrementa en 1 en cada iteración.

Bloque 2:
En este bloque, se recorre una lista de números y se calcula la suma de todos ellos. La variable "sumatoria" se va actualizando en cada iteración, sumando el valor de la variable "número".

Bloque 3:
Aquí se tienen varias palabras en una lista y se concatena cada palabra para formar una oración. La variable "mensaje" se va actualizando en cada iteración, concatenando la palabra actual con las palabras previas.

Bloque 4:
En este bloque, se copia una lista anterior en una nueva lista inicialmente vacía. El método .append() se utiliza para agregar cada elemento de la lista anterior a la nueva lista en cada iteración del bucle "for".

```
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
```
1. Se define una lista llamada "numeros" con varios números.
2. Se crea una lista vacía llamada "menores\_50", la cual almacenará los números menores que 50 de la lista original.
3. Se utiliza un bucle "for" para recorrer cada número en la lista "numeros".
4. En cada iteración, se verifica si el número actual es menor que 50 utilizando la instrucción "if numero < 50".
5. Si el número es menor que 50, se agrega al final de la lista "menores\_50" usando el método .append().
6. Después de recorrer todos los números en la lista "numeros", se imprimen las dos listas: la lista original y la nueva lista con solo números menores que 50.

De esta manera, el código filtra la lista original para crear una nueva lista con solo los números que cumplen con una condición específica (en este caso, ser menores que 50).

```
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
```
1. Definición de la lista de edades:  
   Se crea una lista llamada edades que contiene varias edades.

2. Creación de listas vacías para clasificaciones:  
   Se definen tres listas vacías:
   - menores_18: para almacenar las edades menores de 18.
   - adultos: para almacenar las edades entre 18 y 65.
   - mayores_65: para almacenar las edades mayores de 65.

3. Bucle para clasificar las edades:  
   Se utiliza un bucle for para recorrer cada edad en la lista edades. Para cada edad, se evalúa la condición:
   - Si la edad es menor que 18 (if edad < 18), se agrega a la lista menores_18.
   - Si la edad está entre 18 y 65 (inclusive) (elif edad >= 18 and edad <= 65), se agrega a la lista adultos.
   - Si la edad es mayor de 65 (else), se agrega a la lista mayores_65.

4. Impresión de resultados:  
   Al final, se imprimen las tres listas resultantes junto con la lista original de edades:
   - La lista original (edades).
   - La lista de menores de 18 años (menores_18).
   - La lista de adultos entre 18 y 65 años (adultos).
   - La lista de mayores de 65 años (mayores_65).

Este programa es una excelente manera de mostrar cómo se pueden clasificar datos en diferentes categorías utilizando condiciones en Python.

```
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
```
Ejemplo 1:

En el primer ejemplo, se trata de imprimir los números del 1 al 10 utilizando un bucle "while". Aquí está la explicación paso a paso:

1. Se inicializa la variable "i" en 1.
2. Se utiliza la palabra clave "while" para indicar la condición de parada. En este caso, la condición es que "i" sea menor o igual a 10 (while i <= 10).
3. Dentro del bucle "while", se imprime el valor de la variable "i".
4. Después de imprimir el valor, se incrementa la variable "i" en 1 mediante el operador "+=", que es equivalente a i = i + 1. Esto se repite hasta que la condición de parada se vuelve falsa (es decir, cuando "i" sea mayor que 10).

Ejemplo 2:

En el segundo ejemplo, se imprimen los números del 10 al 1. La estructura del programa es similar al primer ejemplo, pero la condición de parada es diferente (while i >= 1) y la variable "i" se decrementa en cada iteración utilizando el operador "-=", que es equivalente a i = i - 1.

En resumen, este programa muestra dos casos prácticos de los bucles "while" en Python, donde la tarea depende de una condición externa y se desconoce el número de iteraciones necesario para completarla.

```
# programa 9 
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
```
1. Inicialización*: Al igual que en el primer ejemplo, se debe inicializar la variable i antes del bucle (i = 1).

2. Condición del bucle*: El bucle también se ejecutará mientras i sea menor o igual a 10 (while i <= 10:).

3. Condición para evitar un número*: En este caso, hay una condición que verifica si i es igual a 5 (if i == 5:). Si es verdadero, se incrementa i en 1 (i += 1) y luego se utiliza la instrucción continue. Esto hace que el bucle salte al siguiente ciclo sin ejecutar las siguientes líneas de código (es decir, no imprimirá el número 5).

4. Impresión y actualización*: Si i no es igual a 5, se imprime su valor y luego se incrementa en 1.

5. Fin del programa*: Al igual que en el primer ejemplo, después de completar el ciclo (sin importar si fue por alcanzar el límite o por el uso de continue), se imprime "Fin del programa".

Resumen:

- En el primer ejemplo, el programa detiene la ejecución del bucle cuando llega a 5.
- En el segundo ejemplo, evita imprimir el número 5 pero continúa con los demás números hasta llegar a 10.

Ambos ejemplos son útiles para entender cómo controlar la ejecución de los bucles en Python mediante las instrucciones break y continue.

```
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
```
1. Asignación de una cadena de texto*: Se crea una variable llamada cadena y se le asigna una oración en minúsculas: "Python es un lenguaje de programación".
2. Impresión de la cadena original*: Se utiliza print("\n",cadena) para imprimir la cadena original con una línea en blanco antes, para separar la salida.
3. Conversión de la cadena a mayúsculas*: Se crea una nueva variable llamada cadena_mayusculas y se le asigna la cadena cadena convertida a mayúsculas mediante el método .upper(). Este método transforma todas las letras de la cadena a mayúsculas.
4. Impresión de la cadena en mayúsculas*: Se imprime la cadena en mayúsculas, separada por una línea en blanco, utilizando print("\n", cadena_mayusculas).
5. Conversión de la cadena a minúsculas*: Aunque la cadena original ya está en minúsculas, se muestra cómo utilizar el método .lower() para convertir una cadena a minúsculas. Se crea la variable cadena_minusculas y se le asigna la cadena cadena convertida a minúsculas con el método .lower().
6. Impresión de la cadena en minúsculas*: Se imprime la cadena en minúsculas, separada por una línea en blanco, utilizando print("\n", cadena_minusculas).
7. Mensaje de finalización*: Por último, se imprime un mensaje indicando el final del programa, también separado por una línea en blanco, utilizando print("\n Fin del programa").

En resumen, este programa demuestra cómo utilizar los métodos upper() y lower() para convertir las cadenas de texto en Python entre mayúsculas y minúsculas, respectivamente.

```
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
```
1. Inicialización de variables*: Se inicializa una variable llamada palabra como una cadena vacía ("").
2. Condición del bucle*: El bucle "while" se ejecuta mientras la variable palabra sea diferente de la cadena "salir" (while palabra != "salir":).
3. Solicitud de una palabra al usuario*: Dentro del bucle, se utiliza la función input() para solicitar al usuario que ingrese una palabra. La cadena proporcionada se almacena en la variable palabra (palabra = input("Ingresa una palabra o salir para terminar: ")).
4. Conversión de la palabra a minúsculas*: Se utiliza el método lower() para convertir la palabra a minúsculas y almacenarla de nuevo en la variable palabra (palabra = palabra.lower()). Esto garantiza que, si el usuario ingresa "Salir" o "SALIR", la condición de salida del bucle se cumplirá igualmente.
5. Impresión de la palabra ingresada*: Se imprime la palabra ingresada por el usuario junto con un mensaje informativo (print("Usted ingreso:", palabra)).
6. Salida del programa*: Cuando el usuario finalmente ingresa "salir", el bucle termina y se imprime un mensaje indicando el final del programa (print("Fin del programa")).

En resumen, este programa demuestra cómo crear un bucle "while" en Python que se repite hasta que se cumple una determinada condición y cómo utilizar las funciones input() y lower() para interactuar con el usuario y manipular la entrada.

```
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
```
1. Inicialización de variables*: Se inicializa la variable palabra como una cadena vacía ("").
2. Condición del bucle*: En este caso, se utiliza un bucle "while" infinito (while True:). Este bucle se ejecutará indefinidamente hasta que se produzca una interrupción explícita, como una sentencia break.
3. Solicitud de una palabra al usuario*: Al igual que en el programa anterior, se solicita al usuario que ingrese una palabra mediante la función input(), y la cadena proporcionada se almacena en la variable palabra (palabra = input("ingresa una palabra o salir para terminar: ")).

