from selenium.webdriver.common.by import By


class UrbanRoutesPage:

    # ==============================
    # LOCALIZADORES GERAIS
    # ==============================

    FROM_LOCATOR = (
        By.ID,
        "from"
    )

    TO_LOCATOR = (
        By.ID,
        "to"
    )

    PERSONAL_OPTION_LOCATOR = (
        By.XPATH,
        '//div[text()="Personal"]'
    )


    # ==============================
    # SCOOTER
    # ==============================

    SCOOTER_ICON_LOCATOR = (
        By.XPATH,
        '//img[@src="/static/media/scooter.cf9bb57e.svg"]'
    )

    SCOOTER_TEXT_LOCATOR = (
        By.XPATH,
        '//div[contains(text(),"Scooter")]'
    )

    DURATION_TEXT_LOCATOR = (
        By.XPATH,
        '//div[contains(text(),"Duração")]'
    )


    # ==============================
    # BICICLETA
    # ==============================

    BICYCLE_ICON_LOCATOR = (
        By.XPATH,
        '//img[contains(@src,"bike")]'
    )

    BICYCLE_TEXT_LOCATOR = (
        By.XPATH,
        '//div[contains(text(),"Bicicleta")]'
    )


    # ==============================
    # CARSHARING
    # ==============================

    CARSHARING_ICON_LOCATOR = (
        By.XPATH,
        '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]'
    )

    BOOK_BUTTON_LOCATOR = (
        By.XPATH,
        '//button[@class="button round"]'
    )

    CAMPING_TARIFF_LOCATOR = (
        By.XPATH,
        '//div[contains(text(),"Camping")]'
    )

    AUDI_TEXT_LOCATOR = (
        By.XPATH,
        '//div[contains(text(),"Audi A3 Sedã")]'
    )
    # ==============================
    # CARTEIRA DE MOTORISTA
    # ==============================

    ADD_DRIVER_LICENSE_LOCATOR = (
        By.XPATH,
        '(//div[contains(text(),"Adicionar carteira de motorista")])[2]'
    )

    FIRST_NAME_LOCATOR = (
        By.ID,
        "firstName"
    )

    LAST_NAME_LOCATOR = (
        By.ID,
        "lastName"
    )

    DATE_OF_BIRTH_LOCATOR = (
        By.ID,
        "birthDate"
    )

    NUMBER_LOCATOR = (
        By.ID,
        "number"
    )

    ADD_DRIVER_LICENSE_TITLE_LOCATOR = (
        By.XPATH,
        '//div[contains(text(),"Adicionar carteira de motorista")]'
    )

    ADD_BUTTON_LOCATOR = (
        By.XPATH,
        '//form/div[2]/button[1]'
    )

    VERIFICATION_TEXT_LOCATOR = (
        By.XPATH,
        '//div[contains(text(),"Obrigado!")]'
    )

    # ==============================
    # CONSTRUTOR
    # ==============================

    def __init__(self, driver):
        self.driver = driver

    # ==============================
    # MÉTODOS GERAIS
    # ==============================

    def enter_from_location(self, from_text):
        self.driver.find_element(
            *self.FROM_LOCATOR
        ).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(
            *self.TO_LOCATOR
        ).send_keys(to_text)

    # Etapa: inserir De e Para
    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def click_personal_option(self):
        self.driver.find_element(
            *self.PERSONAL_OPTION_LOCATOR
        ).click()


    # ==============================
    # MÉTODOS SCOOTER
    # ==============================

    def click_scooter_icon(self):
        self.driver.find_element(
            *self.SCOOTER_ICON_LOCATOR
        ).click()


    def get_scooter_text(self):
        return self.driver.find_element(
            *self.SCOOTER_TEXT_LOCATOR
        ).text


    def get_duration_text(self):
        return self.driver.find_element(
            *self.DURATION_TEXT_LOCATOR
        ).text



    # ==============================
    # MÉTODOS BICICLETA
    # ==============================

    def click_bicycle_icon(self):
        self.driver.find_element(
            *self.BICYCLE_ICON_LOCATOR
        ).click()


    def get_bicycle_text(self):
        return self.driver.find_element(
            *self.BICYCLE_TEXT_LOCATOR
        ).text



    # ==============================
    # MÉTODOS CARSHARING
    # ==============================

    def click_carsharing_icon(self):
        self.driver.find_element(
            *self.CARSHARING_ICON_LOCATOR
        ).click()



    def click_book_button(self):
        self.driver.find_element(
            *self.BOOK_BUTTON_LOCATOR
        ).click()



    def click_camping(self):
        self.driver.find_element(
            *self.CAMPING_TARIFF_LOCATOR
        ).click()



    def get_audi_text(self):
        return self.driver.find_element(
            *self.AUDI_TEXT_LOCATOR
        ).text



    # ==============================
    # MÉTODOS CARTEIRA DE MOTORISTA
    # ==============================

    def click_add_driver_license(self):
        self.driver.find_element(
            *self.ADD_DRIVER_LICENSE_LOCATOR
        ).click()



    def enter_first_name(self, first_name):
        self.driver.find_element(
            *self.FIRST_NAME_LOCATOR
        ).send_keys(first_name)



    def enter_last_name(self, last_name):
        self.driver.find_element(
            *self.LAST_NAME_LOCATOR
        ).send_keys(last_name)



    def enter_date_of_birth(self, date_of_birth):
        self.driver.find_element(
            *self.DATE_OF_BIRTH_LOCATOR
        ).send_keys(date_of_birth)



    def enter_number(self, number):
        self.driver.find_element(
            *self.NUMBER_LOCATOR
        ).send_keys(number)



    def click_title(self):
        self.driver.find_element(
            *self.ADD_DRIVER_LICENSE_TITLE_LOCATOR
        ).click()



    def click_add_button(self):
        self.driver.find_element(
            *self.ADD_BUTTON_LOCATOR
        ).click()



    def get_verification_text(self):
        return self.driver.find_element(
            *self.VERIFICATION_TEXT_LOCATOR
        ).text



    # ==============================
    # ETAPAS COMBINADAS (POM)
    # ==============================

    def choose_camping_car(self, from_text, to_text):

        self.enter_locations(
            from_text,
            to_text
        )

        self.click_personal_option()

        self.click_carsharing_icon()

        self.click_book_button()

        self.click_camping()



    def adding_driver_license(
            self,
            first_name,
            last_name,
            date_of_birth,
            number):

        self.click_add_driver_license()

        self.enter_first_name(first_name)

        self.enter_last_name(last_name)

        self.enter_date_of_birth(date_of_birth)

        self.enter_number(number)

        self.click_title()

        self.click_add_button()