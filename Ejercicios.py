# 1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena.
#Los espacios no deben ser considerados.

def frecuencia(texto):
    diccionario = {}

    for letra in texto:

        if letra == " ":
            continue

        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1

    return diccionario

texto = "Me gusta programar"

'''
2. Dada una lista de numeros, obten una lista con el doble de cada valor.
'''

lista_numeros = [1,2,3,4,5]

duplicado = list(map(lambda numero : numero * 2, lista_numeros))

print(duplicado)

'''
3. Escribe una funcion que tome una lista de palabras y una palabra objeto como parametros. 
La funcion debe devolver una lista con todas las palabras de la lista origina que contengan la palabra objeto.
'''
def lista_palabra(lista, objetivo):
    resultado_lista = []
    
    for palabra in lista: 
        if objetivo in palabra:
            resultado_lista.append(palabra)
    return resultado_lista

Vehiculos = ['motocicleta', 'coche', 'motor', 'caminon', 'motorizado']
print(lista_palabra(Vehiculos, 'moto'))

'''
4. Genera una funci'on que calcule la diferencia entre valores de dos listas. Usa la funcion map()
'''

def diferencia(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

a = [20, 30, 40]
b = [10, 10, 10]

print(diferencia(a, b))

'''
5. Escribe una funcion que tome una lista de nuemeros como parametro y un valor opcional nota_aprobado (por defecto 5). 
La funci'on deb carcular la media de los numeros de la lista y determinar si la media es mayor o igual a nota_aprobado. 
Si esta es asi el estado sera aprovado de lo contrario sera suspenso. La funcion debe devolver una tupla que contenga la 
media y el estado
'''

def resultados_academicos(notas, nota_aprobado=5) :
    media = sum(notas) / len(notas)

    if media >= nota_aprobado :
        resultado = 'aprobado'
    else :
        resultado = 'suspenso'
    return media, resultado

examenes = resultados_academicos([4.5, 7, 4, 9])

print(examenes)

'''
6. Escribe  un funcion que calcule el factorial de un numero de manera recursiva
'''

def factorial(numero) :
    resultado = 1

    for i in range(1, numero + 1) :
        resultado = resultado * i
    return resultado
print(factorial(6))

'''
7. Genera una funcion que convierta una lista de tuplas a una de strings con la funcion map()
'''

def conversor(lista) :
    return list(map(str, lista))

lista_tuplas = [('ana', 20),('pepe', 25)]
lista_string = conversor(lista_tuplas)
print(lista_string)

'''
8. Escribe un programa que pida al usuario dos numeros e intente dividirlis. Si el usuario ingresa un valor no numerico o
intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la division fue 
exitosa o no.
'''
numeroA = input(f'Intruoduce el dividendo:' )
numeroB = input(f'Introduce el divisor:' )

try :
    numeroA = float(numeroA)
    numeroB = float(numeroB)

    resultado = numeroA / numeroB

except ValueError:
    print('Error: división no exitosa. Debe introducir números')

except ZeroDivisionError:
    print('Error: división no exitosa. No puede dividir entre 0')

else:
    print('División exitosa')
    print(resultado)
    
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def mascotasLegales(mascotas) :
    mascotasProhibidas = ['Mapache', 'Tigre','Serpiente Pitón','Cocodrilo', 'Oso']
    resultado = list(filter(lambda mascotas: mascotas not in mascotasProhibidas, mascotas))
    return resultado

listaMascotas = ['Ratón','Canario', 'Mapache', 'Conejo', 'Cocodrilo', 'Perro', 'Gato']
print(mascotasLegales(listaMascotas))

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def promedio(lista):

    try:
        promedio = sum(lista) / len(lista)

    except ValueError:
        print('error')
        
    except ZeroDivisionError:
        print('error: la lista está vacía')
    else:
        return promedio

numeros = [1, 2, 3, 4, 5]
print(promedio(numeros))

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del 
# rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def edad(años):
    try:
        años = int(años)
        
        if años > 120 or años < 0:
            return 'Edad inválida'
        else :
            return 'Edad registrada con exito'

    except ValueError:

        return 'Introdúzca un número válido'

TuEdad = input(f'Por favor introduzca su edad:')
print(edad(TuEdad))

# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
def Calculadora(frase):
    palabras = frase.split()
    #split: para divicir una cadena en elementos, hay que dividirla para que calcule la longitud de cada palabra
    return list(map(len, palabras))
frase1 = 'La vida es bella'
print(Calculadora(frase1))

# 13. Genera una función que, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
def tuplasCaracteres(Conjunto):
    Conjunto = set(Conjunto)
    return list(map(lambda letra: (letra.upper(), letra.lower()), Conjunto))

Caracteres = 'abdpb'

print(tuplasCaracteres(Caracteres))

# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
def filtroPalabras(lista):
    letra = 'l'
    return list(filter(lambda lista: lista.startswith(letra), lista))

palabras = 'patata', 'laurel', 'comino', 'limon'
print(filtroPalabras(palabras))

#15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumas = [5, 6, 7]

resultado = list(map(lambda numero: numero + 3, sumas))

print(resultado)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros 
# y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
def mayorA(texto):
    numero = 5
    palabras = texto.split()
    return list(filter(lambda palabras: len(palabras) > numero, palabras))

cadena = 'Hoy estaba en el parque de atracciones'
print(mayorA(cadena))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
from functools import reduce

def numero(listaDigitos):
    #Se multiplica por 10 para que de el número: 7*10 = 70 + 8 = 78*10 = 780+2=782
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, listaDigitos)
listanumeros = [7, 8, 9]
print(numero(listanumeros))

# 18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación)
# y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = []

for i in range(3):
    nombre = input(f'Nombre:')
    edad = int(input(f'Edad:'))
    clasificacion = float(input(f'Clasificacion:'))

    estudiante ={
        'Nombre': nombre,
        'Edad': edad,
        'Clasificacion' : clasificacion
    }

    estudiantes.append(estudiante)

print(estudiantes)

sobresaliente = list(filter(lambda estudiante: estudiante['Clasificacion'] >= 90, estudiantes))

print(sobresaliente)

#19.Crea una función lambda que filtre los números impares de una lista dada.
lista = [1, 2, 3, 4, 5]
#un numero par dividido en dos es cero
impares = list(filter(lambda numero: numero % 2 != 0, lista))

print(impares)

#20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
mix = 'Maria', 44, 'Pepe', 25, 'Paloma', 33

#isinstance sirve para saber si un dato es de cierto tipo, en este caso int

edades = list(filter(lambda dato: isinstance(dato, int), mix))

print(edades)
#21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

numero = 3

cubo = lambda numero: numero ** 3

print(cubo(numero))

#22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
from functools import reduce
#La función reduce hay que importarla, porque sino no la detecta ya que no viene incorporada de manera nativa.
#Va acumulando los resultados hasta reducirlos a un resultado

lista = [7, 8, 9]

total = reduce(lambda x, y: x * y, lista)

print(total)

#23. Concatena una lista de palabras. Usa la función reduce().
from functools import reduce

lista = ['Mañana', 'quedamos', 'por', 'la', 'tarde']

frase = reduce(lambda x, y: x + ' ' + y , lista)

print(frase)
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
diferencia = [10, 2, 3]

resultadoDiferencia = reduce(lambda x, y: x - y, diferencia)

print(resultadoDiferencia)

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
from functools import reduce

cadenaTexto = 'Quedamos mañana'

#Sin contar los espacios

def contadorCaracteres(caracteres) :
    palabra = caracteres.split()

    return reduce(lambda x, palabra: x + len(palabra), palabra, 0)

print(contadorCaracteres(cadenaTexto))

#Contando los espacios

def contadoCaracteres2(caracteres):
    return len(caracteres)
print(contadoCaracteres2(cadenaTexto))

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
numeroResto1 = 10
numeroResto2 = 3

restoResultado = lambda x, y : x % y
print(restoResultado(numeroResto1, numeroResto2))

#27. Crea una función que calcule el promedio de una lista de números.
numerospromedio = [7.5, 4, 6.3, 10]
def promedio(numeros) :
    return sum(numeros) / len(numeros)
print(promedio(numerospromedio))

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
duplicados = [4, 3, 7, 5, 4, 9, 7]

def buscadorPrimerDuplicado(lista):
    for numero in lista :
        if lista.count(numero) > 1:
            return numero
    
print(buscadorPrimerDuplicado(duplicados))

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
cadenaEnmascarar = 74965970283720

cadenaEnmascarar = 74965970283720
def enmascarador(digitos):

    digitos = str(digitos)
    #retorna como almohadila todos los digitos excepto los últimos 4 y despues añade los últimos 4 digítos normales
    return '#' * (len(digitos) - 4) + digitos[-4:]

print(enmascarador(cadenaEnmascarar))

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
palabraAnagrama1 = 'casco'
palabraAnagrama2 = 'cacos'
palabraAnagrama3 = 'jamon'
palabraAnagrama4 = 'monje'

def anagramas(palabra1, palabra2):
    #sorted ordena los elemento de una lista, en este caso, por orden alfabético por lo que si tinen las mismas letras coincidirán totalmente en orden
    if sorted(palabra1) == sorted(palabra2):
        return 'Son anagramas'
    else:
        return 'No son anagramas'

print(anagramas(palabraAnagrama1,palabraAnagrama2))
print(anagramas(palabraAnagrama3,palabraAnagrama4))

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
#En este primer caso, la lista la intorduce el usuario
def introduzcaLista():
    #se pone el split para separar cada dato que se introduzca separado por la coma
    dato = input("Introduce los nombres separados por comas y sin espacios: ").split(",")
    busqueda = input("Nombre a buscar: ")

    try:
        if busqueda in dato:
            return "Nombre encontrado"
        else:
            raise Exception("Nombre no encontrado")

    except Exception as error:
        return error


print(introduzcaLista())
#En este segundo caso sería con una lista ya dada

def introduzcaLista2(dato):

    busqueda = input("Nombre a buscar: ")

    try:
        if busqueda in dato:
            return "Nombre encontrado"
        else:
            raise Exception("Nombre no encontrado")

    except Exception as error:
        return error


nombresLista = ["Ana", "Luis", "Marta", "Pedro"]

print(introduzcaLista2(nombresLista))

#32.Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
Empleados = [
    {'nombre': 'Manuel Rodriguez', 'puesto': 'Atención al cliente'},
    {'nombre': 'María Barrio', 'puesto': 'Jefa de sección'},
    {'nombre': 'Ruben Torres', 'puesto': 'Soporte it'}]
Busqueda = str(input(f'Introduzca el nombre'))

def FiltroEmpleados(lista, busqueda):
    for empleado in lista:
        #se pone lo de .lower para que no hay problemas de mayúsculas o minúsculas al realizar la busqueda, ya que lo pasa todo a minúsculas.
        if empleado ['nombre'].lower() == busqueda.lower():
            return empleado['puesto']
    return 'No trabaja aquí'
print(FiltroEmpleados(Empleados,Busqueda))

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

sumaListas = list(map(lambda x, y: x + y, lista1, lista2))
print(sumaListas)

#34. Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.\
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Código a seguir:\
# Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.\
# Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.\
# Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.\
# Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.\
# Implementar el método quitar_rama para eliminar una rama en una posición específica.\
# Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.\
# Caso de uso:\
#         a. Crear un árbol.\
#         b. Hacer crecer el tronco una unidad.\
#         c. Añadir una nueva rama.\
#         d. Hacer crecer todas las ramas una unidad.\
#         e. Añadir dos nuevas ramas.\
#         f. Retirar la rama situada en la posición 2.\
#         g. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    def crecer_tronco(self):
        self.tronco += 1
    def nueva_rama(self):
        self.ramas.append(1)
    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
    def quitar_rama(self, position):
        self.ramas.pop(position)
    def info_arbol(self):
        return {
            'Logitud del tronco': self.tronco,
            'Ramas': len(self.ramas),
            'Longitud de las ramas': self.ramas
        }
#En este ejercicio, tuve que ejecutar dos veces la fución nueva rama, para que pudeira haber tres ramas y poder eliminar la rama de la posición 2,

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)

print(arbol.tronco)
print(arbol.ramas)
print(arbol.info_arbol())

# 35. Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.\
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.\
# Código a seguir:\
# Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.\
# Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.\
# Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.\
# Implementar agregar_dinero para aumentar el saldo del usuario.\
# Caso de uso:\
#         a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.\
#         b. Agregar 20 unidades al saldo de Bob.\
#         c. Transferir 80 unidades de Bob a Alicia.\
#         d. Retirar 50 unidades del saldo de Alicia.\
class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError("No hay saldo suficiente")

    def transferir_dinero(self, usuario, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            usuario.saldo += cantidad
        else:
            raise ValueError("No hay saldo suficiente")


alicia = UsuarioBanco("Alicia", 100, True)
#En esta parte tuve que cambiar los datos del enunciado ya que sino, bob tenía la cuenta en negativo y no se podía retornar un resultado
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)

try:
    bob.transferir_dinero(alicia, 80)
except ValueError as error:
    print(error)

alicia.retirar_dinero(50)

print(bob.saldo)
print(alicia.saldo)

# 36. Crea una función llamada procesar_texto**\
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.\
# Código a seguir:\
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.\
# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.\
# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.\
# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.\
# Caso de uso:\
# Verificar el funcionamiento completo de procesar_texto.

def contar_palabras(texto):
    palabras = texto.split()
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    return texto.replace(palabra, "")

def procesar_texto(texto, opcion, *args):

    if opcion == 'contar':
        return contar_palabras(texto)

    elif opcion == 'reemplazar':
        #arg[0] es la palabra al remplazar
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == 'eliminar':
        return eliminar_palabra(texto, args[0])

frase = 'Mañana vamos a la playa'
print(procesar_texto(frase, 'contar'))
print(procesar_texto(frase, 'reemplazar', 'playa', 'montaña'))
print(procesar_texto(frase, 'eliminar', 'Mañana'))

#37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
hora = int(input('Introduce la hora:'))

if hora <= 6:
    print("Es de noche")

elif 7 <= hora <= 12:
    print("Es de día")

elif 13 <= hora <= 20:
    print("Es de tarde")

elif 21 <= hora <= 23:
    print("Es de noche")

else:
    print("Hora no válida")

# 38 Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.\
# Reglas:\
#         0 - 69: insuficiente\
#         70 - 79: bien\
#         80 - 89: muy bien\
#         90 - 100: excelente
nota = int(input('Introduce tu nota:'))
if nota <= 69:
    print('Insuficiente')
elif 70 <= nota <= 79:
    print('Bien')
elif 80 <= nota <= 89:
    print('Muy bien')
elif 90 <= nota <= 100:
    print('Encelente')
else:
    print('error')

# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    elif figura == "circulo":
        radio = datos[0]
        return 3.1416 * radio ** 2

    else:
        return "Figura no válida"

print(calcular_area("circulo", (4,)))

#40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:**\
    # a. Solicitar al usuario el precio original de un artículo.\
    # b. Preguntar si tiene un cupón de descuento (respuesta sí o no).\
    # c. Si la respuesta es sí, solicitar el valor del cupón de descuento.\
    # d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).\
    # e. Mostrar el precio final de la compra, considerando o no el descuento.\
    # f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.\
precio = float(input('Introduzca el precio:'))
cupon = input('¿Tiene cupón? (Sí/No):').lower()

if cupon == "Sí":

    descuento = float(input("Introduce el valor del descuento: "))

    if descuento > 0:
        precio_final = precio - descuento
        print(f"El precio final es: {precio_final} €")
    else:
        print("El cupón no es válido")
        print(f"El precio final es: {precio} €")

elif cupon == "no":

    print(f"El precio final es: {precio} €")

else:

    print("Respuesta no válida")