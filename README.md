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

python
mascota = input("Ingresa el tipo de mascota: ")


2. Verifica si el valor de la variable "mascota" contiene la palabra "perro":

python
if "perro" in mascota:
    print("Es un perro")


Si la palabra "perro" está presente en la variable "mascota", se imprimirá "Es un perro" en la consola.

3. En caso de que la palabra "perro" no esté presente en la variable "mascota", se procede a verificar si la entrada contiene la palabra "gato" mediante la condición "elif":

python
elif "gato" in mascota:
    print("Tienes un gato")


Si la variable "mascota" contiene la palabra "gato", se imprimirá "Tienes un gato" en la consola.

4. Si ninguna de las condiciones anteriores se cumple, se llega a la condición "else". Esta condición indica que ninguna de las palabras buscadas ("perro" o "gato") está presente en la variable "mascota":

python
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

python
n1 = int(input("ingresa el numero 1: "))
n2 = int(input("ingresa el numero 2: "))


2. Se utiliza una condición "if" para verificar si el valor de "n1" es mayor que el de "n2":

python
if n1 > n2:
    print ("El numero " + str(n1) + " es mayor al " + str (n2))


Si la condición se cumple, se imprimirá un mensaje en la consola indicando que el primer número ingresado es mayor que el segundo número.

3. En caso de que la condición "if" no se cumpla, el programa continúa con la condición "elif" para verificar si los valores de "n1" y "n2" son iguales:

python
elif n1 == n2:
    print("Son números iguales")


Si la condición "elif" se cumple, se imprimirá un mensaje en la consola indicando que los números ingresados son iguales.

4. Si ninguna de las condiciones anteriores se cumple, se concluye que el valor de "n1" es menor que el de "n2". En este caso, se ejecuta la condición "else" y se imprime un mensaje en la consola indicando que el primer número es menor que el segundo:

python
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

python
variable = input("Ingresa tu edad: ")


En Python, la función input() siempre devuelve una cadena de texto (str), sin importar si la entrada consiste en números o letras.

2. Se imprime el tipo de dato de la variable "variable" utilizando la función "type()":

python
print(type(variable))


Esto imprimirá <class 'str'> en la consola, ya que la entrada del usuario se almacena como una cadena de texto (str).

3. Se convierte la entrada del usuario a un número entero (int) y se almacena en la misma variable "variable":

python
variable = int(variable) #Convertir la variable a tipo entero


Esto convertirá la entrada del usuario en un número entero, siempre y cuando la entrada sea una cadena de texto numérica válida.

4. Se imprime nuevamente el tipo de dato de la variable "variable":

python
print(type(variable))


Ahora se imprimirá <class 'int'> en la consola, debido a que la variable ha sido convertida a un entero.

5. Se convierte la variable "variable" a un número flotante (float):

python
variable = float(variable) #Convertir la variable a tipo flotante


6. Se imprime nuevamente el tipo de dato de la variable "variable":

python
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

python
def calcular_impuesto(ingreso):


2. Se definen las condiciones para calcular el impuesto según la tabla. Si el ingreso es menor o igual a 1000, se aplica un 5% de impuesto:

python
    if ingreso <= 1000:
        impuesto = ingreso * 0.05


3. Si el ingreso está entre 1001 y 2500, se aplica un 8% de impuesto:

python
    elif ingreso >1000 and ingreso <= 2500:
        impuesto = ingreso * 0.08


4. Si el ingreso está entre 2501 y 6000, se aplica un 12% de impuesto:

python
    elif ingreso >2500 and ingreso < 6000:
        impuesto = ingreso * 0.12


5. Si el ingreso es mayor o igual a 6000, se aplica un 15% de impuesto:

python
    elif ingreso >= 6000:
        impuesto = ingreso * 0.15


6. En caso de que el ingreso no se ajuste a las condiciones anteriores, se calcula el impuesto usando todos los rangos de impuestos:

python
    else:
        impuesto = (1000 * 0.05) + (2500 * 0.08) + (2501 * 0.12) + (6000 * 0.15)


7. La función devuelve el cálculo del impuesto:

python
    return impuesto


Luego, se solicita al usuario que ingrese su ingreso, se llama a la función para calcular el impuesto y se calcula el salario final restando el impuesto del ingreso. Finalmente, se muestran los resultados en pantalla:

python
# Solicitar el ingreso al usuario
ingreso_empleado = float(input("¿Cuales son tus ingresos?: "))
impuesto_a_pagar = calcular_impuesto(ingreso_empleado)

# Calcular el salario final
salario_final = ingreso_empleado - impuesto_a_pagar

# Mostrar resultados
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

python
calificación = float(input("Calificación del estudiante (0-100): "))


2. Se define una variable "desempeño" que almacenará el nivel de desempeño del estudiante. Se utiliza una estructura de control "if-elif-else" para evaluar la calificación:

python
if calificacion <= 60:
    desempeño = "Insuficiente"


Si la calificación es menor o igual a 60, se asigna el valor "Insuficiente" a la variable "desempeño".

python
elif 60 < calificación <= 79 :
    desempeño = "Suficiente"


Si la calificación está entre 60 y 79 (ambos inclusive), se asigna el valor "Suficiente" a la variable "desempeño".

python
elif 79 < calificación <= 89:
    desempeño = "Muy bien"


Si la calificación está entre 79 y 89 (ambos inclusive), se asigna el valor "Muy bien" a la variable "desempeño".

python
elif 89 < calificación <= 95:
    desempeño = "Notable"


Si la calificación está entre 89 y 95 (ambos inclusive), se asigna el valor "Notable" a la variable "desempeño".

python
elif 95 < calificación <= 100:
    desempeño = "Excelente"


Si la calificación está entre 95 y 100 (ambos inclusive), se asigna el valor "Excelente" a la variable "desempeño".

3. Se imprime el nivel de desempeño del estudiante:

python
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

python
print("Lista de enteros")
print(["5, 8, 10"])


La lista contiene las cadenas "5", "8" y "10" separadas por comas y entre corchetes. Al imprimirla, se mostrarán los elementos de la lista entre corchetes y separados por comas.

2. Se crea una lista de textos (strings) y se imprime:

python
print("\nLista de textos")
print(["Manzana", "Piña", "Naranja"])


Esta lista contiene las cadenas "Manzana", "Piña" y "Naranja" separadas por comas y entre corchetes. Al imprimirla, se mostrarán los elementos de la lista entre corchetes y separados por comas.

3. Se crea una lista de booleanos y se imprime:

python
print("\nLista de booleanos")
print(["True, False, True"])


En este caso, la lista contiene las cadenas "True", "False" y "True", separadas por comas y entre corchetes. Al imprimirla, se mostrarán los elementos de la lista entre corchetes y separados por comas.

4. Se crea una lista vacía y se imprime:

python
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

python
cadenas = ["Juan", "Pedro", "Chuy"]


2. Se imprime la lista completa:

python
print(cadenas)


Al imprimir la lista, se mostrarán todos los elementos entre corchetes y separados por comas: ['Juan', 'Pedro', 'Chuy'].

3. Se imprime el segundo elemento de la lista (Pedro) accediendo al índice 1 de la lista:

python
print(cadenas[1])


El resultado será Pedro.

4. Se imprime el tipo de dato de la lista utilizando la función type():

python
print(type(cadenas))


El tipo de dato de la lista es <class 'list'>, lo que significa que es una lista en Python.

5. Se imprime el tipo de dato del segundo elemento de la lista (Pedro) utilizando la función type():

python
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

python
print("Indexing")


2. Se crea una lista de números y se imprimen elementos específicos utilizando indexación:

python
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

python
print("\nSubscripting")


4. Se crea una lista de nombres y se imprimen segmentos de la lista usando segmentación:

python
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

python
puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_texto = ["10", "20", "30"]


2. Se imprime la comparación de igualdad entre las listas "puntos" y "puntos\_2" usando el operador ==:

python
print(puntos==puntos_2) #True


El resultado será True ya que las listas son idénticas en contenido y orden.

3. Se imprime la comparación de igualdad entre las listas "puntos" y "ordenados" usando el operador ==:

python
print(puntos==ordenados) #False


El resultado será False ya que, aunque tienen los mismos elementos, las listas tienen diferente orden.

4. Se imprime la comparación de igualdad entre las listas "puntos" y "puntos\_texto" usando el operador ==:

python
print(puntos==puntos_texto) #False


El resultado será False ya que las listas tienen contenido diferente: una contiene enteros y la otra contiene strings (cadenas de texto).

5. Se imprime la comparación de desigualdad entre las listas "puntos" y "puntos\_2" usando el operador !=:

python
print(puntos!=puntos_2) #False


El resultado será False ya que las listas son idénticas en contenido y orden.

6. Se imprime la comparación de desigualdad entre las listas "puntos" y "ordenados" usando el operador !=:

python
print(puntos!=ordenados) #True


El resultado será True ya que las listas tienen diferente orden.

7. Se imprime la comparación de desigualdad entre las listas "puntos" y "puntos\_texto" usando el operador !=:

python
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

python
nombres = ["Choto", "Emilio", "Luis"]


2. Se imprime la verificación de la membresía del elemento "Luis" en la lista "nombres" usando el operador in:

python
print("Luis" in nombres) #True


El resultado será True ya que el elemento "Luis" se encuentra en la lista.

3. Se imprime la verificación de la membresía del elemento "Emi" en la lista "nombres" usando el operador in:

python
print("Emi" in nombres) #False


El resultado será False ya que el elemento "Emi" no se encuentra en la lista.

4. Se imprime la verificación de la membresía del elemento "Javier" en la lista "nombres" usando el operador in:

python
print("Javier" in nombres) #False


El resultado será False ya que el elemento "Javier" no se encuentra en la lista.

5. Se imprime la verificación de la membresía del elemento "Jose" en la lista "nombres" usando el operador not in:

python
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

python
colores = ["rojo", "azul"]


2. Se imprime la lista "colores":

python
print(colores)


La salida será ['rojo', 'azul'].

3. Se utiliza el método append() para agregar un nuevo elemento a la lista "colores":

python
colores.append("verde")


El método append() agrega el elemento "verde" al final de la lista.

4. Se imprime la lista "colores" luego de agregar el elemento "verde":

python
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

python
mi_lista = ["Rojo", "Verde", "Morado", "Azul", "Naranja"]


2. Se utiliza el método pop() para eliminar y devolver el último elemento de la lista. Luego, se imprimen el elemento eliminado y la lista después de utilizar pop():

python
# Usamos pop para eliminar y devolver el último elemento
ultimo_elemento = mi_lista.pop()
print("Elemento eliminado:", ultimo_elemento)
print("Lista después de usar pop:", mi_lista)


El resultado será:
yaml
Elemento eliminado: Naranja
Lista después de usar pop: ['Rojo', 'Verde', 'Morado', 'Azul']


3. Se utiliza el método pop() con el argumento 1 para eliminar y devolver el elemento en la posición 1 (índice 1) de la lista. Luego, se imprimen el elemento eliminado y la lista después de utilizar pop():

python
# Usamos pop para eliminar y devolver el elemento en la posición 1
elemento_en_posicion_1 = mi_lista.pop(1)
print("Elemento eliminado en la posición 1:", elemento_en_posicion_1)
print("Lista después de usar pop en la posición 1:", mi_lista)


El resultado será:
yaml
Elemento eliminado en la posición 1: Verde
Lista después de usar pop en la posición 1: ['Rojo', 'Morado', 'Azul']


Este programa muestra cómo eliminar y devolver elementos de una lista en Python utilizando el método pop(). Puede eliminar tanto el último elemento (sin argumentos) como un elemento en una posición específica (con un argumento de índice).
