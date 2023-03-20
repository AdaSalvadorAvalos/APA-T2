"""
Ada Salvador Avalos


"""


# Esta función se hizo en clase de laboratorio.
def esPrimo(numero):
    """
    Devuelve `True` si su argumento es primo, y `False` si no lo es.
    La función tiene como argumento un número.

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """
    for prueba in range(2,int(numero**0.5)+1):
        if numero%prueba == 0 : return False
    
    return True


# Esta función se hizo en clase de laboratorio.
def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.
    La función tiene como argumento un número.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([ prueba for prueba in range(2, numero) if esPrimo(prueba) ])


# Esta función se hizo en clase de laboratorio.
def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento.
    La función tiene como argumento un número.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """
    factores=[] # lista vacia
    for factor in primos(numero):
        while numero%factor == 0:
            factores.append(factor)
            numero //= factor
    return tuple(factores)


    # Esta lo hice antes de clase, y aunque no usa primos(), funciona.
    #i= 2
    #factor = []
    #while range(2,numero):

    #    if numero%i==0:
    #        numero= numero//i
    #       factor.append(i)
    #  else : 
    #     i=i+1
    #return tuple(factor)


def dicFact(numero1, *numero2):
    """
    Devuelve el factor primo de un número con su correspondiente exponente.
    La función tiene como argumento uno o varios números.

    >>> dicFact(90, 14)
    ({2: 1, 3: 2, 5: 1, 7: 0}, {2: 1, 3: 0, 5: 0, 7: 1})
    """
    factores1 = descompon(numero1)
    factores2 = []   #lista vacía
    for numero in numero2:
        factores2.extend(descompon(numero)) # descompone el numero2 en factores primos  
        #y si se suma la lista creada a la lista factores2
    
    factores = set(list(factores1) + list(factores2)) #se suman factores1 y factores2
    #transformándolos en listas.
    dicfact1 = {factor: 0 for factor in factores}
    dicfact2 = {factor: 0 for factor in factores}
    for factor in factores1: dicfact1[factor] += 1
    for factor in factores2: dicfact2[factor] += 1
    return dicfact1, dicfact2


# Esta función se hizo en clase de laboratorio.
def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    La función tiene como argumento dos números.

    >>> mcm(90, 14)
    630
    """
    mcm = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcm *= factor ** max(dicFact1[factor],dicFact2[factor])
    return mcm
    

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    La función tiene como argumento n números.

    >>> mcmN(90, 14, 28, 35)
    1260
    """
    dicFactNumeros = [dicFact(numero) for numero in numeros] if len(numeros) > 1 else [dicFact(numeros[0])]
    #se crea una lista dicFactNumeros que contiene los diccionarios de factores primos de cada número
    #que se pasa como argumento . Si se pasa solo un número se crea una lista con solo un diccionario de factores primos para
    #ese número
    factores = set() # conjunto vacío
    for df1, df2 in dicFactNumeros:
        factores.update(df1.keys()) #actualiza la clave del diccionario 1 y se suma a factores
        factores.update(df2.keys()) #actualiza la clave del diccionario 2 y se suma a factores
    mcmN = 1
    for factor in factores:
        mcmN *= factor ** max(dicFact1.get(factor, 0) for dicFact1, dicFact2 in dicFactNumeros) #se usa get para poder acceder al 
        #valor de la clave del diccionario, si no está devuelve 0.
    return mcmN





def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    La función tiene como argumento dos números.

    >>> mcd(924, 780)
    12
    """
    mcd = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcd *= factor ** min(dicFact1[factor],dicFact2[factor])
    return mcd
    
def mcdN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    La función tiene como argumento n números.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    dicFactNumeros = [dicFact(numero) for numero in numeros] if len(numeros) > 1 else [dicFact(numeros[0])]
    factores = set()
    for df1, df2 in dicFactNumeros:
        factores.update(df1.keys())
        factores.update(df2.keys())
    mcdN = 1
    for factor in factores:
        mcdN *= factor ** min(dicFact1.get(factor, 0) for dicFact1, dicFact2 in dicFactNumeros) 
    return mcdN


import doctest
doctest.testmod()