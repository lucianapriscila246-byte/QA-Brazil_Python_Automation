import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage

def test_adding_license():
    # Importa o módulo time para criar pausas durante o teste
    import time

    # Importa o Selenium para abrir e controlar o navegador
    from selenium import webdriver

    # Importa a classe POM com os métodos da página
    from urban_routes_main_page import UrbanRoutesPage

    # Cria o teste
    def test_adding_license():
        # ==============================
        # ABRIR O NAVEGADOR
        # ==============================

        driver = webdriver.Chrome()

        # Abrir o Urban Routes da Tarefa 3
        driver.get(
            "https://cnt-8de30f7f-f57a-4215-9c96-e573ca6b9b29.containerhub.tripleten-services.com?lng=pt"
        )

        # Esperar a página carregar
        time.sleep(10)

        # ==============================
        # CRIAR OBJETO DA PÁGINA (POM)
        # ==============================

        urban_routes_page = UrbanRoutesPage(driver)

        # ==============================
        # PREENCHER ENDEREÇOS
        # ==============================

        # Inserir endereço "De"
        urban_routes_page.enter_from_location(
            "East 2nd Street, 601"
        )

        # Inserir endereço "Para"
        urban_routes_page.enter_to_location(
            "1300 1st St"
        )

        # ==============================
        # ESCOLHER PERSONAL
        # ==============================

        urban_routes_page.click_personal_option()

        time.sleep(2)

        # ==============================
        # ESCOLHER CARSHARING
        # ==============================

        urban_routes_page.click_carsharing_icon()

        time.sleep(2)

        # ==============================
        # CLICAR EM RESERVAR
        # ==============================

        urban_routes_page.click_book_button()

        time.sleep(3)

        # ==============================
        # ESCOLHER TARIFA CAMPING
        # ==============================

        urban_routes_page.click_camping_tariff()

        time.sleep(3)

        # ==============================
        # ADICIONAR CARTEIRA DE MOTORISTA
        # ==============================

        urban_routes_page.click_add_driver_license()

        time.sleep(2)

        # Preencher Nome
        urban_routes_page.enter_first_name(
            "Luciana"
        )

        # Preencher Sobrenome
        urban_routes_page.enter_last_name(
            "Silva"
        )

        # Preencher Data de nascimento
        urban_routes_page.enter_date_of_birth(
            "01/01/1996"
        )

        # Preencher Número da carteira
        urban_routes_page.enter_license_number(
            "123456789"
        )

        # Clicar no título "Adicionar uma carteira de motorista"
        urban_routes_page.click_add_license_title()

        time.sleep(1)

        # Clicar em outro lugar para ativar botão (bug do navegador)
        urban_routes_page.click_add_license_title()

        time.sleep(1)

        # Clicar botão Adicionar
        urban_routes_page.click_add_button()

        time.sleep(3)

        # ==============================
        # VERIFICAR RESULTADO
        # ==============================

        actual_value = urban_routes_page.get_thanks_text()

        expected_value = "Obrigado!"

        assert expected_value in actual_value, (
            f"Esperado '{expected_value}', mas apareceu '{actual_value}'"
        )

        # Fechar navegador
        driver.quit()