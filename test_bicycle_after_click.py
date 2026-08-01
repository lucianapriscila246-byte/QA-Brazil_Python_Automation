# Importa tempo para pequenas pausas
import time


# Importa Selenium
from selenium import webdriver


# Importa nosso arquivo POM
from urban_routes_main_page import UrbanRoutesPage



# Cria o teste
def test_personal_bicycle_option():

    # Abre o navegador
    driver = webdriver.Chrome()


    # Abre o servidor atual
    driver.get(
        "https://cnt-1c2e009b-3247-4001-8223-a86534e32c1a.containerhub.tripleten-services.com?lng=pt"
    )


    # Espera a página carregar
    time.sleep(3)



    # Cria uma página usando o POM
    urban_routes_page = UrbanRoutesPage(driver)



    # Preenche campo De
    urban_routes_page.enter_from_location(
        "East 2nd Street, 601"
    )


    # Preenche campo Para
    urban_routes_page.enter_to_location(
        "1300 1st St"
    )



    # Clica em Personal
    urban_routes_page.click_personal_option()


    time.sleep(2)



    # Clica na Bicicleta
    urban_routes_page.click_bicycle_icon()


    time.sleep(2)



    # Pega o texto Bicicleta
    actual_value = urban_routes_page.get_bicycle_text()



    # Texto esperado
    expected_value = "Bicicleta"



    # Confirma que apareceu Bicicleta
    assert expected_value in actual_value



    # Fecha navegador
    driver.quit()