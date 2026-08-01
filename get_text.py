# Importa a ferramenta Selenium para controlar o navegador
from selenium import webdriver

# Importa a classe By para localizar elementos na página
from selenium.webdriver.common.by import By

# Importa o tempo para criar pequenas pausas durante o teste
import time


# Cria o navegador Chrome controlado pelo Selenium
driver = webdriver.Chrome()


# Abre a página do Urban Routes
# (troque pelo link do seu servidor quando necessário)
driver.get("https://cnt-12b6d93a-6105-44e1-a0aa-b8fb7192f307.containerhub.tripleten-services.com?lng=pt")


# Aguarda 2 segundos para a página carregar completamente
time.sleep(2)


# Encontra o elemento que contém o texto "PLATFORM"
# Usa o nome da classe CSS: logo-disclaimer
# Depois pega apenas o texto desse elemento usando .text
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text


# Verifica se o texto encontrado é exatamente "PLATFORM"
# Se estiver correto, o teste continua
# Se estiver errado, o teste falha
assert disclaimer == "PLATFORM"


# Mostra no terminal o texto encontrado
print(disclaimer)


# Fecha o navegador e encerra o teste
driver.quit()