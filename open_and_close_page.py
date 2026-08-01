# Importa o Selenium para controlar o navegador
from selenium import webdriver

# Cria uma conexão com o Chrome
driver = webdriver.Chrome()

# Abre a página do Urban Routes
driver.get("https://cnt-7ae3cea6-071f-4194-bd78-db2f11e9d589.containerhub.tripleten-services.com?lng=pt")

# Verifica se a URL contém o endereço esperado
assert "tripleten-services.com" in driver.current_url

# Fecha o navegador
driver.quit()