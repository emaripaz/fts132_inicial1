import time
from unittest import case

import pytest  # Framework de Teste Unitário
import requests  # Framework de Teste de API - Requests / Responses

# Endereço da API

base_url = 'https://petstore.swagger.io/v2/user/'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'
token_usuario = ''


# Os teste
def testar_criar_usuario():
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '4576'


# Executa
    resposta = requests.post(  # Faz a requisição, passando:
        url=base_url,  # O endpoint da API
        data=open('C:/Users/Rafael/Desktop/Mariana/Iterasys/fts132_inicial/Test/db/user1.json', 'rb'),  # O body JSON
        headers=headers  # O header com o Content-Type
    )

# Formatação
    corpo_da_resposta = resposta.json()  # Formata com json
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada



def testar_consultar_usuario():
# Configura
    status_code = 200
    id = 4576
    username = 'vic'
    firstName = 'victoria'
    lastName = 'cali'
    email = 'vic.vic@teste.com.br'
    password = 'vicvic'
    phone = '2244443333'
    userStatus = 0

# Executa
    resposta = requests.get(
        url=f'{base_url}{username}',
        headers=headers
    )

# Formata
    corpo_da_resposta = resposta.json()  # Formata com json
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)

# Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta ['id'] == id
    assert corpo_da_resposta ['username'] == username
    assert corpo_da_resposta ['email'] == email
    assert corpo_da_resposta ['phone'] == phone

    print(f'Token: {token_usuario}')

def testar_consultar_usuario_com_token (token_usuario):
# Configura
    status_code = 200
    id = 4576
    username = 'vic'
    firstName = 'victoria'
    lastName = 'cali'
    email = 'vic.vic@teste.com.br'
    password = 'vicvic'
    phone = '2244443333'
    userStatus = 0

# Executa
    resposta = requests.get(
        url=f'{base_url}{username}',
        headers=headers
    )

# Formata
    corpo_da_resposta = resposta.json()  # Formata com json
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)

# Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta ['id'] == id
    assert corpo_da_resposta ['username'] == username
    assert corpo_da_resposta ['email'] == email
    assert corpo_da_resposta ['phone'] == phone

    print(f'Token: {token_usuario}')

def testar_alterar_usuario():
#Configura
    username = 'vic'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '4576'

#Executa
    resposta = requests.put(
        url=f'{base_url}{username}',
        data=open('C:/Users/Rafael/Desktop/Mariana/Iterasys/fts132_inicial/Test/db/user2.json', 'rb'),
        headers = headers
    )

#Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

#Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_excluir_usuario():
    #Configura
    username = 'vic'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'vic'

    #Executar
    resposta = requests.delete(
        url=f'{base_url}{username}',
        headers=headers
    )

#Formatação

    match resposta.status_code:
        case 200 :
            corpo_da_resposta = resposta.json()
            print(resposta)
            print(resposta.status_code)
            print(corpo_da_resposta)

#Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

    match resposta.status_code:

        case 400 :
            print('username fornecido incorreto')
        case 404 :
            print('usuário não encontrado')

def testar_login_do_usuario ():
#Configura
    username = 'vic'
    password = 'vicvic'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'

#Executa
    resposta = requests.get(
        url=f'{base_url}login?username={username}&password={password}',
        headers = headers
    )

#Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

#Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'].find (inicio_mensagem_esperada) != -1

    frase = 'Neste fim de ano, planeje o seu sucesso!'
    assert frase.find ('sucesso') != -1

#Extrair
#Na mensagem "logged in user session:1639489800123" queremos pegar os números
    mensagem_recebida = corpo_da_resposta['message']
    print(f'A mensagem recebida é: {mensagem_recebida}')
    token_usuario = mensagem_recebida[23:37]
    print(f'O Token do usuário é: {token_usuario}')
    testar_consultar_usuario_com_token(token_usuario)

#Exemplo
    frase = "Saldo: R$1.987,65"
    valor = frase [7:17]
    print(f'O Valor é: {valor}')

#TODO: Controlar o tempo entre as requisições na sequência
'''
def testar_sequencia_de_testes ():
    testar_criar_usuario()
    testar_login_do_usuario()
    testar_alterar_usuario()
    testar_consultar_usuario()
    testar_excluir_usuario()
'''
