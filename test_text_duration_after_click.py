import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage


def test_duration_personal_scooter_option():

    # Abrir navegador
    driver = webdriver.Chrome()

    # Abrir Urban Routes
    driver.get(
        "https://cnt-95e3fb77-7346-4c41-9681-75d7607de138.containerhub.tripleten-services.com?lng=pt"
    )

    time.sleep(5)

    # Criar objeto POM
    urban_routes_page = UrbanRoutesPage(driver)

    # Inserir os endereços usando a nova etapa
    urban_routes_page.enter_locations(
        "East 2nd Street, 601",
        "1300 1st St"
    )

    # Escolher Personal
    urban_routes_page.click_personal_option()

    time.sleep(2)

    # Escolher Scooter
    urban_routes_page.click_scooter_icon()

    time.sleep(2)

    # Verificar texto Duração
    actual_value = urban_routes_page.get_duration_text()

    expected_value = "Duração"

    assert expected_value in actual_value

    driver.quit()