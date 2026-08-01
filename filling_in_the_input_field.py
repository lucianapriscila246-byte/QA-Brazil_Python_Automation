# Importa o módulo de tempo para criar pequenas pausas no teste
import time

# Importa o Selenium WebDriver para controlar o navegador
from selenium import webdriver

# Importa a classe By para localizar elementos na página
from selenium.webdriver.common.by import By

# Importa condições prontas de espera do Selenium
from selenium.webdriver.support import expected_conditions

# Importa a ferramenta de espera explícita
from selenium.webdriver.support.wait import WebDriverWait


# Cria o driver que conecta o Python ao navegador Chrome
driver = webdriver.Chrome()

# Abre a página do Urban Routes (coloque aqui o link do seu servidor)
driver.get("https://cnt-ef54a0b9-8bf6-47fc-a19e-00245a32de46.containerhub.tripleten-services.com?lng=pt")


# Aguarda 2 segundos para a página carregar completamente
time.sleep(2)


# Encontra o campo "De" pelo ID e digita o endereço de partida
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")


# Encontra o campo "Para" pelo ID e digita o endereço de chegada
driver.find_element(By.ID, "to").send_keys("1300 1st St")


# Aguarda 2 segundos para visualizar o preenchimento
time.sleep(2)


# Encontra o botão "Chamar um táxi" usando XPath e clica nele
driver.find_element(By.XPATH, "//button[@class='button round']").click()


# Espera até que o campo de comentário apareça e esteja visível
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.ID, "comment"))
)


# Encontra o campo de comentário e escreve uma mensagem para o motorista
driver.find_element(By.ID, "comment").send_keys("Olá")


# Aguarda 2 segundos para visualizar o resultado
time.sleep(2)


# Verifica se o comentário digitado é exatamente o esperado
assert driver.find_element(By.ID, "comment").get_attribute("value") == "Olá"


# Fecha o navegador e encerra a sessão do Selenium
driver.quit()