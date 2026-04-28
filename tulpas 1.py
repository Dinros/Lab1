def esPar(num):
    """ 
    Funcionamiento: Determina si un número es par
    Entradas:
    num(int): número entero a evaluar
    Salidas:
    bool: True si el número es par, False en caso contrario
    """
    if num % 2 == 0:
        return True
    else:
        return False

def contarParesImpares(tulpla):
    """ 
    Funcionamiento: Cuenta la cantidad de números pares e impares dentro de una tupla, validando previamente que los números sean de hasta 4 dígitos
    Entradas:
    tulpla(tuple): tupla de números enteros
    Salidas:
    tuple: (cantidad de pares, cantidad de impares) si la validación es correcta
    str: mensaje de error si algún número no cumple la condición
    """
    pares = 0
    impares = 0
    for par in tulpla:
        if esPar(par):
            pares += 1
        else:
            impares += 1
    return (pares, impares)

def contarParesImparesAUX(tulpla):
    """ 
    Funcionamiento: Verifica que todos los números de la tupla sean menores o iguales a 4 dígitos
    Entradas:
    tulpla(tuple): tupla de números enteros
    Salidas:
    bool: True si todos los números cumplen la condición, False si alguno es mayor a 9999
    """
    if isinstance(tulpla, tuple) == True:
        for num in tulpla:
            if num > 9999 or num < 1000:
                return "Todos los numeros deben ser de 4 dígitos"
        return contarParesImpares(tulpla)

def separarParesImpares(ptupla): 
    """
    Funcionamiento:
    Separa los dígitos pares e impares de números naturales de 4 dígitos.
    Entradas:
    - ptupla(tuple): tupla con números naturales de 4 dígitos
    Salida:
    - (tuple): una tupla con lista de pares y lista de impares
    """
    listaPares = []
    listaImpares = []
    for num in ptupla:
        if isinstance(num, int) == False or num < 1000 or num > 9999:
            return "Debe ser un número natural de 4 dígitos"
        if esPar(num) == True:
            listaPares.append(num)
        else:
            listaImpares.append(num)
    return (listaPares,listaImpares)

def esPerfecto(num):
    """ 
    Funcionamiento: Determina si un número es perfecto sumando sus divisores propios positivos
    Entradas:
    num(int): número entero positivo a evaluar
    Salidas:
    bool: True si el número es perfecto, False en caso contrario
    """
    suma = 0
    for i in range(1, num): 
        if num % i == 0: 
            suma += i
    if suma == num:
        return True
    else:
        return False


def esNumPerfecto(tupla):
    """ 
    Funcionamiento: Recibe una tupla de exactamente 5 números y devuelve una lista con los números perfectos encontrados
    Entradas:
    tupla(tuple): tupla de números enteros
    Salidas:
    list: lista con los números perfectos encontrados
    str: mensaje indicando error de cantidad o ausencia de números perfectos
    """
    if len(tupla) != 5:
        return "Debe indicar exactamente 5 valores de entrada para analizar."
    resultados = []
    for num in tupla:
        if esPerfecto(num):
            resultados.append(num)
    if len(resultados) > 0:
        return resultados
    else:
        return "No hay números perfectos"

def obtenerDiferencia (ptupla):
    """
    Funcionamiento:
    Retorna la diferencia simétrica de dos números enteros.
    Entradas:
    - ptupla(tuple): tupla con dos números enteros
    Salida:
    - (int/bool/string): diferencia simétrica, False o mensaje de error
    """
    if isinstance(ptupla,tuple) == False:
        return "Debe recibir una tupla para analizar los valores."
    if len(ptupla) != 2:
        return "Debe recibir una tupla para analizar los valores." 
    num1 = ptupla[0]
    num2 = ptupla[1]
    if isinstance(num1,int) == False or isinstance(num2,int) == False:
        return "Ambos valores deben ser enteros."
    if num1 <= 0 or num2 <=0:
        return "Ambos valores deben ser mayores a 0."
    str1 = str(num1)
    str2 = str(num2)
    resultado = ""
    for digito in str1:
        if digito not in str2 and digito not in resultado:
            resultado += digito
    for digito in str2:
        if digito not in str1 and digito not in resultado:
            resultado += digito
    if resultado == "":
        return False
    return int(resultado)

# def extras
def verbosInfinitivos(palabra):
    """
    Funcionamiento: Recibe una palabra y devuelve True si la palabra es un verbo en infinitivo, de lo contrario devuelve False
    Entradas:
    palabra(str): una palabra
    Salidas:
    bool: devuelve True si la palabra es un verbo en infinitivo, de lo contrario devuelve False
    """
    if palabra[-1] == "ar" or palabra[-1] == "er" or palabra[-1] == "ir" or palabra[-1] == "or" or palabra[-1] == "ur":
        return True
    return False

def esPar(n):
    """
    Funcionamiento: Recibe un numero entero y devuelve True si el numero es par, de lo contrario devuelve False
    Entradas:
    n(int): numero entero
    Salidas:
    resultado(bool): devuelve True si el numero es par, de lo contrario devuelve False
    """
    if n%2 == 0:
        return True
    return False

def palabraReves(palabra):
    """
    Funcionamiento: Recibe una palabra y devuelve la palabra al reves
    Entradas:
    palabra(str): una palabra
    Salidas:
    resultado(str): la palabra al reves
    """
    i = -1
    c = len(palabra)
    resultado = ""
    while c > 0:
        resultado += palabra[i]
        c -= 1
        i -= 1
    return resultado

def sumaDivisores(n):
    """
    Funcionamiento: Recibe un numero entero positivo y devuelve la suma de sus divisores
    Entradas:
    n(int): numero entero positivo
    Salidas:
    resultado(int): la suma de los divisores del numero dado
    """
    resultado = 0
    for i in range(1,n):
        if n%i == 0:
            resultado += i
    return resultado

# Def 
def verbosInfinitivos(palabra):
    """
    Funcionamiento: Recibe una palabra y devuelve True si la palabra es un verbo en infinitivo, de lo contrario devuelve False
    Entradas:
    palabra(str): una palabra
    Salidas:
    bool: devuelve True si la palabra es un verbo en infinitivo, de lo contrario devuelve False
    """
    if palabra[-1] == "ar" or palabra[-1] == "er" or palabra[-1] == "ir" or palabra[-1] == "or" or palabra[-1] == "ur":
        return True
    return False
def palabraReves(palabra):
    """
    Funcionamiento: Recibe una palabra y devuelve la palabra al reves
    Entradas:
    palabra(str): una palabra
    Salidas:
    resultado(str): la palabra al reves
    """
    i = -1
    cont = len(palabra)
    resultado = ""
    while cont > 0:
        resultado += palabra[i]
        cont -= 1
        i -= 1
    return resultado

def sumaDivisores(n):
    """
    Funcionamiento: Recibe un numero entero positivo y devuelve la suma de sus divisores
    Entradas:
    n(int): numero entero positivo
    Salidas:
    resultado(int): la suma de los divisores del numero dado
    """
    resultado = 0
    for i in range(1,n):
        if n%i == 0:
            resultado += i
    return resultado
#reto 7 categorizar palabras
def categorizarPalabras(ptupla):
    """
    Funcionamiento: Recibe una tupla con frases, y devuelve una lista con los verbos infinitivos y las palabras palindromas
    Entradas:
    ptupla(tuple): una tupla con frases
    Salidas:
    resultado(list): una lista con los verbos infinitivos y las palabras palindromas
    """
    resultado = []
    resultado1 = []
    for i in ptupla:
        resultado1 = []
        lista = []
        palindromos = []
        palabras = i.split()
        for l in palabras:
            l = l.lower()
            if verbosInfinitivos(l) == True:
                lista += [l]
            if len(l) > 1:
                if palabraReves(l) == l:
                    palindromos += [l]
        resultado1.append(lista)
        if len(palindromos) != 0:
            resultado1.append(palindromos)
        resultado.append(resultado1)
    return resultado

def categorizarPalabrasAux(ptupla):
    """
    Funcionamiento: Verifica que las entradas sean una tupla con frases, y llama a la funcion categorizarPalabras para devolver una lista con los verbos infinitivos y las palabras palindromas
    Entradas:
    ptupla(tuple): una tupla con frases
    Salidas:
    string: devuelve un mensaje de error si las entradas no son validas
    list: una lista con los verbos infinitivos y las palabras palindromas
    """
    if isinstance(ptupla,tuple) == False:
        return "Debe ingresar una tupla"
    for i in ptupla:
        if isinstance(i,str) == False:
            return "Los elementos ingresados en la tupla deben ser frases"
    return categorizarPalabras(ptupla)

# reto 11 pares amigables
def esParAmigable(ptupla):
    """
    Funcionamiento: recibe una tupla con dos numumeros, para saber si la suma del primer numero es igual al segundo
    Entradas:
    ptupla(tuple): una tupla que contiene dos numeros enteros positivos
    Salidas:
    resultado(bool): devuelve True si la suma de los divisores del primer numero es igual al segundo numero, de lo contrario devuelve False
    """
    if sumaDivisores(ptupla[0]) == ptupla[1]:
        return True
    return False
def esParAmigableAux(ptupla):
    """
    Funcionamiento: verifica que las entradas sean una tupla con dos numeros enteros positivos y llama a la funcion esParAmigable para saber si la suma del primer numero es igual al segundo
    Entradas:
    ptupla(tuple): una tupla que contiene dos numeros enteros positivos
    Salidas:
    string: devuelve un mensaje de error si las entradas no son validas
    (bool): devuelve True si la suma de los divisores del primer numero es igual al segundo numero, de lo contrario devuelve False
    """
    if ptupla[0] == ptupla[1]:
        return "Los numeros ingresados en la tupla deben ser diferentes entre si"
    if isinstance(ptupla,tuple) == False:
        return "Debe ingresar una tupla"
    if len(ptupla) != 2:
        return "Debe ingresar una tupla con dos numeros enteros positivos"
    for i in ptupla:
        if isinstance(i,int) == False or i < 0:
            return "Los elementos ingresados en la tupla deben ser numeros enteros positivos"
    return esParAmigable(ptupla)

#PP




print("="*20+"Ejercicio 1"+"="*20+"\n"+"="*20+"Contar la cantidad de impares"+"="*20)
print(contarParesImparesAUX((1235, 1742, 1111, 2321)))
print(contarParesImparesAUX((2426, 1224, 1542, 1000)))
print(contarParesImparesAUX((3557,1237,1243)))
print(contarParesImparesAUX((219999, )))

print("="*20+"Ejercicio 3"+"="*20+"\n"+"="*20+"Separar pares e impares"+"="*20)
print(separarParesImpares((1235,1742,1111,2321)))
print(separarParesImpares((2426,1224,1542,1000)))
print(separarParesImpares((3557,1237,1111,2321)))
print(separarParesImpares((3557,)))
print(separarParesImpares((219999,)))

print("="*20+"Ejercicio 5"+"="*20+"\n"+"="*20+"Localizando los números perfectos"+"="*20)
print(esNumPerfecto((6,123,45,496,17)))
print(esNumPerfecto((100,15,28,51,4)))
print(esNumPerfecto((8128,75,28,12,1000)))
print(esNumPerfecto((750,122,14,3,1550)))
print(esNumPerfecto((10,23,33550336,125,750)))
print(esNumPerfecto((2,)))

print("Reto 7 categorizar palabras")
print("Entradas: ", ("Cantar llorar y reír que más pedir a la vida", "Reconocer las salas del museo es bueno",))
print("Salidas: ",categorizarPalabrasAux(("Cantar llorar y reír que más pedir a la vida", "Reconocer las salas del museo es bueno")))
print("Entradas: ",("Ana tiene su radar en el ojo siempre"))
print("Salidas: ",categorizarPalabrasAux(("Ana tiene su radar en el ojo siempre",)))
print("Entradas: ",("Equivocarse es de humanos"))
print("Salidas: ",categorizarPalabrasAux(("Equivocarse es de humanos",)))
print("Entradas: ", "Equivocarse es de humanos")
print("Salidas: ",categorizarPalabrasAux("Equivocarse es de humanos"))
print()

print("="*20+"Ejercicio 9"+"="*20+"\n"+"="*20+"Obtener diferencia simétrica"+"="*20)
print(obtenerDiferencia((1265,42)))
print(obtenerDiferencia((88587,71457)))
print(obtenerDiferencia((542,254)))
print(obtenerDiferencia((2984,48298)))
print(obtenerDiferencia((12345,67890)))
print(obtenerDiferencia((1,1010)))
print(obtenerDiferencia((-21,1010)))
print(obtenerDiferencia((1,1010.6)))
print(obtenerDiferencia([12345,67890]))

print("Reto 11 pares amigables")
print("Entradas: ", (220, 284))
print("Salidas: ",esParAmigableAux((220, 284)))
print("Entradas: ", (15,18))
print("Salidas: ",esParAmigableAux((15,18)))
print("Entradas: ", (1184, 1210))
print("Salidas: ",esParAmigableAux((1184, 1210)))
print("Entradas: ", (890,890))
print("Salidas: ",esParAmigableAux((890,890)))
print()