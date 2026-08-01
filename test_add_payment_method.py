import data
import helpers

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()

        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        cls.driver = webdriver.Chrome(options=options)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")

    def test_add_payment_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)

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

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()