import data
import helpers

from selenium import webdriver
from pages import UrbanRoutesPage
from selenium.webdriver.chrome.options import Options


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes.")

        options = Options()

        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        cls.driver = webdriver.Chrome(options=options)

        cls.driver.get(data.URBAN_ROUTES_URL)


    def test_set_route(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO


    def test_select_plan(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        routes_page.select_supportive_plan()

        assert routes_page.get_current_selected_plan() == "Comfort"

    def test_fill_phone_number(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        routes_page.set_phone(data.PHONE_NUMBER)

        routes_page.confirm_phone()

        assert routes_page.get_phone() == data.PHONE_NUMBER

    def test_order_taxi(self):

        routes_page = UrbanRoutesPage(self.driver)

        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page.set_route(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        routes_page.select_supportive_plan()

        routes_page.set_phone(
            data.PHONE_NUMBER
        )

        routes_page.confirm_phone()

        routes_page.click_payment_method()

        routes_page.click_add_card()

        routes_page.set_card_number(
            data.CARD_NUMBER
        )

        routes_page.set_card_code(
            data.CARD_CODE
        )

        routes_page.click_card_add_confirm()

        routes_page.close_payment_popup()
        routes_page.wait_overlay_disappear()

        routes_page.set_driver_message(
            data.MESSAGE_FOR_DRIVER
        )

        routes_page.select_blanket()
        assert routes_page.is_blanket_selected() is True

        routes_page.add_two_ice_creams()

        assert routes_page.get_ice_cream_count() == "2"

        routes_page.click_order_taxi()

        assert "Buscar carro" in routes_page.get_driver_arrival_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()