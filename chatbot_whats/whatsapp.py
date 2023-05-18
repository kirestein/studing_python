# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(30)
# Definir contatos e grupos e mensagem a ser enviada
contatos = ['kza', 'Elisete de Souza']
mensagem = 'Oiê, estou testando aqui.'
# Buscar contatos/grupos
def buscar_contato(contato):
    """ campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "selectable-text copyable-text")]')
    campo_pesquisa = driver.find_element(By.XPATH, '//div[contains(@class, "selectable-text copyable-text")]') 
    !NENHUM DOS DOIS COMANDOS FUNCIONARAM, REVER O CÓDIGO!
    """
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
for contato in contatos:
    buscar_contato(contato)
    # enviar_mensagem(mensagem)
    # selectable-text copyable-text
# enviar mensagens
    # selectable-text copyable-text