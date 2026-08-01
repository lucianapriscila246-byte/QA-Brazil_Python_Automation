from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)


    def test_personal_bike_option(self):

        self.driver.get('https://cnt-714a3a39-bce5-4125-8581-5e2685e19387.containerhub.tripleten-services.com?lng=pt')

        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_locations(
            'East 2nd Street, 601',
            '1300 1st St'
        )

        urban_routes_page.click_personal_option()

        time.sleep(2)

        urban_routes_page.click_bicycle_icon()

        time.sleep(2)

        actual_value = urban_routes_page.get_bicycle_text()

        expected_value = "Bicicleta"

        assert expected_value in actual_value


    def test_duration_personal_bike_option(self):

        self.driver.get('https://cnt-714a3a39-bce5-4125-8581-5e2685e19387.containerhub.tripleten-services.com?lng=pt')

        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_locations(
            'East 2nd Street, 601',
            '1300 1st St'
        )

        urban_routes_page.click_personal_option()

        time.sleep(2)

        urban_routes_page.click_bicycle_icon()

        time.sleep(2)

        actual_value = urban_routes_page.get_duration_text()

        expected_value = "Duração"

        assert expected_value in actual_value


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()