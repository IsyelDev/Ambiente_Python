

def multiplicacion(*args):
    result =1
    for numero in args:
        result*=numero
    return result

print(multiplicacion(2,2,3))


def concatenar(**kwargs):
    resulta = ""
    print(kwargs.items())
    print(kwargs.values())
    print(kwargs.keys())
    for letra in kwargs.values():
        resulta+=letra
    return resulta

concatenar(primero="hola", segundos="nuevo")

print(concatenar(a="Codo",b="Tam",c="cas"))


multiplicar = lambda x : x*2
b = multiplicar(5)

print(b)



class ValorInvalido(Exception):
    pass


def validarNumero(n):
    if n<0:
        raise ValorInvalido("El valor es invalido")
    
try:
  validarNumero(-1)
except ValorInvalido as e:
  print(f'An exception occurred {e}') 
  
  
sumatoria = lambda a,b : a + b
print(sumatoria(15,12))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = list(filter(lambda x : x%2!=0,numeros))
print(impares)

cuadrado = list(map(lambda x : x**2,numeros))
print(cuadrado)

from functools import reduce

sumarr = reduce(lambda x,y : x+y,numeros)
print(sumarr)   


tuplas = [(1, 3), (2, 1), (3, 2)]

# Usamos lambda para ordenar por el segundo valor
ordenadas = sorted(tuplas, key=lambda x: x[1])

print(ordenadas)  # Resultado: [(2, 1), (3, 2), (1, 3)]


numero_par = lambda xx : 'Par' if xx % 2 == 0 else "Impar"
resultt = [numero_par(x) for x in numeros]
print(resultt)


