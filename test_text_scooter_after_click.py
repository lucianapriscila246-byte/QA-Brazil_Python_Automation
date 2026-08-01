import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage


def test_personal_scooter_option():

    driver = webdriver.Chrome()

    driver.get(
        "https://cnt-ffb8ce40-270a-4ee2-9399-77412692b5f6.containerhub.tripleten-services.com?lng=pt"
    )

    time.sleep(5)

    print(driver.current_url)
    print(driver.title)


    urban_routes_page = UrbanRoutesPage(driver)


    urban_routes_page.enter_from_location(
        "East 2nd Street, 601"
    )


    urban_routes_page.enter_to_location(
        "1300 1st St"
    )


    urban_routes_page.click_personal_option()

    time.sleep(2)


    urban_routes_page.click_scooter_icon()

    time.sleep(2)


    actual_value = urban_routes_page.get_scooter_text()

    expected_value = "Scooter"


    assert expected_value in actual_value


    driver.quit()