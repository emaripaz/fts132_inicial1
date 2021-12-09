import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros, \
    elevar_um_numero_pelo_outro, calcular_a_area_do_quadrado, calcular_a_area_do_triangulo, calcular_a_area_do_circulo, \
    calcular_a_area_do_retangulo

somar_dois_numeros, subtrair_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros, \
    elevar_um_numero_pelo_outro, calcular_a_area_do_quadrado, calcular_a_area_do_retangulo, \
    calcular_a_area_do_triangulo, calcular_a_area_do_circulo


def testar_somar_dois_numeros():
    num1 = 6
    num2 = 2
    resultado_esperado = 8
    resultado_atual = somar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_subtrair_dois_numeros():
    num1 = 6
    num2 = 2
    resultado_esperado = 4
    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_dividir_dois_numeros():
    num1 = 6
    num2 = 2
    resultado_esperado = 3
    resultado_atual = dividir_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_multiplicar_dois_numeros():
    num1 = 6
    num2 = 2
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


def testar_calcular_a_area_do_triangulo():
    num1 = 5
    num2 = 2
    resultado_esperado = 5
    resultado_atual = calcular_a_area_do_triangulo(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_a_area_do_circulo():
    raio = 1
    resultado_esperado = 3.14
    resultado_atual = calcular_a_area_do_circulo(raio)
    assert resultado_atual == resultado_esperado
