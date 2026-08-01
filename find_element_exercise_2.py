# Importa a biblioteca para criar pausas
import time

# Importa o Selenium WebDriver
from selenium import webdriver

# Importa a classe By para localizar elementos
from selenium.webdriver.common.by import By

# Cria uma instância do navegador Chrome
driver = webdriver.Chrome()

# Abre o Urban Routes
driver.get("https://cnt-d22d9bfb-05ff-4d12-b742-1ab654ff4d2e.containerhub.tripleten-services.com?lng=pt")

# Aguarda a página carregar completamente
time.sleep(2)

# Encontra todos os elementos com a classe "dst-picker-marker" usando XPath
elements = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")

# Verifica se foram encontrados mais de um elemento
assert len(elements) > 1

# Fecha o navegador
driver.quit()