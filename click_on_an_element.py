# Importa a biblioteca para criar pausas
import time

# Importa o Selenium WebDriver
from selenium import webdriver

# Importa a classe By para localizar elementos
from selenium.webdriver.common.by import By

# Cria uma instância do navegador Chrome
driver = webdriver.Chrome()

# Abre o Urban Routes
driver.get("https://cnt-eb6d134f-7733-4e61-8f52-eb9c2d634320.containerhub.tripleten-services.com?lng=pt")

# Aguarda a página carregar completamente
time.sleep(2)

# Encontra o botão "X" pelo XPath e clica nele
driver.find_element(
    By.XPATH,
    "//button[@class='close-button input-close-button']"
).click()

# Aguarda 2 segundos para visualizar o resultado
time.sleep(2)

# Fecha o navegador
driver.quit()