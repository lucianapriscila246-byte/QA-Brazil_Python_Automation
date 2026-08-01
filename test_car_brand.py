import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage


def test_car_brand():

    # Abrir navegador
    driver = webdriver.Chrome()


    # Abrir Urban Routes
    driver.get(
        "https://cnt-ffb8ce40-270a-4ee2-9399-77412692b5f6.containerhub.tripleten-services.com?lng=pt"
    )


    # Esperar carregar
    time.sleep(5)



    # Criar objeto POM
    urban_routes_page = UrbanRoutesPage(driver)



    # Preencher campo De
    urban_routes_page.enter_from_location(
        "East 2nd Street, 601"
    )


    # Preencher campo Para
    urban_routes_page.enter_to_location(
        "1300 1st St"
    )



    # Escolher Personal
    urban_routes_page.click_personal_option()

    time.sleep(2)



    # Escolher Carsharing
    urban_routes_page.click_carsharing_icon()

    time.sleep(2)



    # Clicar Reservar
    urban_routes_page.click_book_button()

    time.sleep(2)



    # Escolher tarifa Camping
    urban_routes_page.click_camping_tariff()

    time.sleep(2)



    # Verificar marca do carro
    actual_value = urban_routes_page.get_car_brand_text()

    expected_value = "Audi A3 Sedã"


    # Confirmar resultado
    assert expected_value in actual_value



    # Fechar navegador
    driver.quit()