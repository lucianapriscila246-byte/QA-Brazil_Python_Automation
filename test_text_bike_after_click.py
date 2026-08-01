import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage


def test_personal_bike_option():

    # Abrir o navegador Chrome
    driver = webdriver.Chrome()

    # Abrir o aplicativo Urban Routes usando o link do servidor atual
    driver.get(
        "https://cnt-ffb8ce40-270a-4ee2-9399-77412692b5f6.containerhub.tripleten-services.com?lng=pt"
    )

    # Esperar a página carregar
    time.sleep(5)

    # Criar uma instância da classe POM
    # Agora podemos usar os métodos criados no urban_routes_main_page.py
    urban_routes_page = UrbanRoutesPage(driver)


    # Inserir endereço no campo "De"
    urban_routes_page.enter_from_location(
        "East 2nd Street, 601"
    )


    # Inserir endereço no campo "Para"
    urban_routes_page.enter_to_location(
        "1300 1st St"
    )


    # Clicar na opção "Personal"
    urban_routes_page.click_personal_option()

    # Esperar para carregar as opções de transporte
    time.sleep(2)


    # Clicar no ícone "Bicicleta"
    urban_routes_page.click_bicycle_icon()

    # Esperar para aparecer o texto Bicicleta
    time.sleep(2)


    # Pegar o texto exibido na página
    actual_value = urban_routes_page.get_bicycle_text()

    # Texto que esperamos encontrar
    expected_value = "Bicicleta"


    # Verificar se o texto esperado aparece na página
    assert expected_value in actual_value


    # Fechar o navegador
    driver.quit()