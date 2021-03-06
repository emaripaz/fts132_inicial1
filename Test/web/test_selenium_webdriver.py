# 1 Importar Bibliotecas
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest


caminho_print = 'C:/Users/Rafael/Desktop/Mariana/Iterasys/fts132_inicial/prints/'\
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'


# 2 Classe
class Test_selenium_webdriver():

    # Definição de início - Executa antes do teste
    def setup_method(self):
        # Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome('C:/Users/Rafael/Desktop/Mariana/Iterasys/fts132_inicial/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O site vai esperar até 30 segundos pelos elementos
        self.driver.maximize_window()  # Maximizar a janela do navegdor

        #Cria a pasta caminho_print apenas antes do primeiro teste
        try:
            os.mkdir(caminho_print)
        except:
            print('A pasta já existia')



    # Definição de fim - executa depois do teste
    def teardown_method(self):
        # Destruiur o objeto do Selenium
        self.driver.quit()

    # Definição do teste
    @pytest.mark.parametrize('id, termo, curso, preco', [
        ('1', 'mantis', 'Mantis', 'R$ 59,99'),
        ('2', 'ctfl', 'Preparatório CTFL', 'R$ 199,00'),
        ('3', 'java', 'Fundamentos do Java', 'R$ 149,00'),
        ])
    def testar_comprar_curso_com_click_na_lupa(self, id, termo, curso, preco):

        # O selenium abre a url indicada - site alvo do teste
        self.driver.get('http://www.iterasys.com.br')
        self.driver.get_screenshot_as_file(f'{caminho_print} teste {id} passo 1 - home.png')
        # O selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O selenium apaga o conteúdo da caixa  de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve "mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.get_screenshot_as_file(f'{caminho_print} teste {id} passo 2 - pesquisa_pelo_nome.png')
        # O selenium clica no botão da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O selenium clica em 'matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):
        # O selenium abre a url indicada - site alvo do teste
        self.driver.get('http://www.iterasys.com.br')
        # O selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O selenium apaga o conteúdo da caixa  de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve "mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # O selenium pressiona a tecla enter
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(Keys.ENTER)
        # O selenium clica em 'matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == "Mantis"
        # O selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

    def testar_comprar_curso_ctfl_com_click_na_lupa(self):
        # O selenium abre a url indicada - site alvo do teste
        self.driver.get('http://www.iterasys.com.br')
        # O selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O selenium apaga o conteúdo da caixa  de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve "mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('ctfl')
        # O selenium clica no botão da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O selenium clica em 'matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == "Preparatório CTFL"
        # O selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 199,00'