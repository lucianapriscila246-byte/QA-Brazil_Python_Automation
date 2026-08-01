# Importa o módulo time para criar pequenas pausas
import time

# Importa o Selenium para controlar o navegador
from selenium import webdriver

# Importa a classe POM
from urban_routes_main_page import UrbanRoutesPage


# ==============================
# TESTE CAMPING
# ==============================

def test_camping():

    # ==============================
    # ABRIR O NAVEGADOR
    # ==============================

    driver = webdriver.Chrome()

    # Abrir o Urban Routes
    driver.get(
        "https://cnt-fd23f14a-07bd-4208-ba60-364876e43374.containerhub.tripleten-services.com?lng=pt"
    )

    # Esperar a página carregar
    time.sleep(5)


    # ==============================
    # CRIAR OBJETO POM
    # ==============================

    urban_routes_page = UrbanRoutesPage(driver)


    # ==============================
    # ESCOLHER O CARRO CAMPING
    # ==============================

    urban_routes_page.choose_camping_car(
        "East 2nd Street, 601",
        "1300 1st St"
    )

    time.sleep(2)


    # ==============================
    # ADICIONAR CARTEIRA
    # ==============================

    urban_routes_page.adding_driver_license(
        "Luciana",
        "Silva",
        "01/01/1996",
        "123456789"
    )

    time.sleep(3)


    # ==============================
    # VERIFICAR RESULTADO
    # ==============================

    actual_value = urban_routes_page.get_thanks_text()

    expected_value = "Obrigado!"

    assert expected_value in actual_value


    # ==============================
    # FECHAR NAVEGADOR
    # ==============================

    driver.quit()