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

        routes_page.select_supportive_plan()

        routes_page.set_phone(data.PHONE_NUMBER)

        assert routes_page.get_phone() == data.PHONE_NUMBER

    def test_confirm_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.click_next_button()

        code = retrieve_phone_code(self.driver)

        routes_page.set_code(code)

        routes_page.click_confirm_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()