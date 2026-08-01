# Importa a biblioteca para fazer pausas
import time

# Importa o Selenium WebDriver
from selenium import webdriver

# Importa a classe By para localizar elementos na página
from selenium.webdriver.common.by import By

# Cria uma instância do navegador Chrome
driver = webdriver.Chrome()

# Abre o site (substitua pela URL do seu servidor)
driver.get("https://cnt-d22d9bfb-05ff-4d12-b742-1ab654ff4d2e.containerhub.tripleten-services.com?lng=pt")

# Aguarda 2 segundos para a página carregar completamente
time.sleep(2)

# Encontra o logotipo usando um seletor CSS
element = driver.find_element(By.CSS_SELECTOR, "img.logo-image")

# Exibe no terminal o elemento encontrado
print(element)

# Fecha o navegador e encerra a sessão do Selenium
driver.quit()