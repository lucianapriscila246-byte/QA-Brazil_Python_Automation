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

# Encontra o campo "De" pelo ID
from_field = driver.find_element(By.ID, "from")

# Encontra o campo "Para" pelo ID
to_field = driver.find_element(By.ID, "to")

# Verifica se o placeholder do campo "De" está correto
assert from_field.get_attribute("placeholder") == "East 2nd Street, 601"

# Verifica se o placeholder do campo "Para" está correto
assert to_field.get_attribute("placeholder") == "1300 1st St"

# Fecha o navegador
driver.quit()