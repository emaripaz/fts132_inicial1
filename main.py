import pytest
import soma as soma


def somar_dois_numeros(num1, num2):
    return num1 + num2


def subtrair_dois_numeros(num1, num2):
    return num1 - num2


def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'

def multiplicar_dois_numeros(num1, num2):
        return num1 * num2

def elevar_um_numero_pelo_outro (num1, num2):
    return num1 ** num2

def calcular_a_area_do_quadrado (num1):
    return num1 * num1

def calcular_a_area_do_retangulo (num1, num2):
    return num1 * num2

def calcular_a_area_do_triangulo (num1, num2):
    return num1 * num2 / 2

def calcular_a_area_do_circulo (raio):
    return 3.14 * raio ** 2

if __name__ == '__main__':
    soma = somar_dois_numeros(1, 2)
    print(f'O resultado da soma é {soma}')

    subtracao = subtrair_dois_numeros(3, 4)
    print(f'O resultado da subtração é {subtracao}')

    divisao = dividir_dois_numeros(6, 0)
    print(f'O resultado da divisão é {divisao}')

    multiplicacao = multiplicar_dois_numeros(2, 3)
    print(f'O resultado da multiplicação é {multiplicacao}')

    exponenciacao = elevar_um_numero_pelo_outro(2, 3)
    print(f'O resultado da exponenciação é {exponenciacao}')

    area_do_quadrado = calcular_a_area_do_quadrado(3)
    print(f'A área do quadrado é {area_do_quadrado}')

    area_do_retangulo = calcular_a_area_do_retangulo (3, 2)
    print(f'A área do retangulo é {area_do_retangulo}')

    area_do_triangulo = calcular_a_area_do_triangulo(5, 2)
    print(f'A área do triângulo é {area_do_triangulo}')

'''
def testar_somar_dois_numeros ():
    num1 = 6
    num2 = 2
    resultado_esperado = 8
    resultado_atual = somar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_subtrair_dois_numeros ():
    num1 = 6
    num2 = 2
    resultado_esperado = 4
    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_dividir_dois_numeros ():
    num1 = 6
    num2 = 2
    resultado_esperado = 3
    resultado_atual = dividir_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_multiplicar_dois_numeros():
    num1 = 6
    num2 = 2
    #teste
    resultado_esperado = 12
    resultado_atual = multiplicar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_elevar_um_numero_pelo_outro():
    num1 = 6
    num2 = 2
    resultado_esperado = 36
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_a_area_do_quadrado():
    num1 = 6
    resultado_esperado = 36
    resultado_atual = calcular_a_area_do_quadrado(num1)
    assert resultado_atual == resultado_esperado
    
def testar_calcular_a_area_do_retangulo():
    num1 = 6
    num2 = 2
    resultado_esperado = 12
    resultado_atual = calcular_a_area_do_retangulo(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_a_area_do_triangulo ():
    num1 = 5
    num2 = 2
    resultado_esperado = 5
    resltado_atual = calcular_a_area_do_triangulo(num1, num2)
    assert resltado_atual == resultado_esperado
'''