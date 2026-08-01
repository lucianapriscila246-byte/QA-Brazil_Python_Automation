from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code


class UrbanRoutesPage:

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    PHONE_CONTROL = (
        By.CLASS_NAME,
        "np-button"
    )

    PHONE_VALUE = (
        By.XPATH,
        "//div[@class='np-text' and contains(text(), '+1')]"
    )

    PHONE_FIELD = (
        By.ID,
        "phone"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Próximo')]"
    )

    CODE_FIELD = (
        By.ID,
        "code"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Confirmar')]"
    )

    TARIFF_CARDS = (
        By.CLASS_NAME,
        "tcard"
    )

    SELECTED_TARIFF = (
        By.XPATH,
        "//div[contains(@class,'tcard active')]"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Pedir')]"
    )

    PAYMENT_METHOD = (
        By.XPATH,
        "//div[contains(@class,'pp-button') and .//div[contains(text(),'Método de pagamento')]]"
    )

    ADD_CARD_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'pp-row') and contains(.,'Adicionar cartão')]"
    )

    CARD_NUMBER_FIELD = (
        By.ID,
        "number"
    )

    CARD_CODE_FIELD = (
        By.XPATH,
        "//input[@id='code' and @placeholder='12']"
    )

    ADD_CARD_CONFIRM_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Adicionar') and not(@disabled)]"
    )

    CLOSE_PAYMENT_BUTTON = (
        By.CLASS_NAME,
        "section-close"
    )


    CARD_PLUS = (
        By.CLASS_NAME,
        "pp-plus"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def set_from_field(self, address):
        self.get_from_field().send_keys(address)


    def set_to_field(self, address):
        self.get_to_field().send_keys(address)


    def get_from_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.FROM_FIELD)
        )

    def get_to_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TO_FIELD)
        )

    def get_from(self):
        return self.get_from_field().get_attribute("value")

    def get_to(self):
        return self.get_to_field().get_attribute("value")

    def set_route(self, from_address, to_address):
        self.set_from_field(from_address)
        self.set_to_field(to_address)
        self.click_call_taxi()

    def click_call_taxi(self):
        button = (
            By.XPATH,
            "//button[contains(text(),'Chamar um táxi')]"
        )

        self.wait.until(
            EC.element_to_be_clickable(button)
        ).click()

    def set_phone(self, phone_number):
        self.wait.until(
            EC.element_to_be_clickable(self.PHONE_CONTROL)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.PHONE_FIELD)
        ).send_keys(phone_number)

    def select_comfort_tariff(self):
        cards = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.TARIFF_CARDS
            )
        )

        cards[4].click()

    def select_supportive_plan(self):
        self.select_comfort_tariff()


    def get_selected_plan(self):

        active = (
            By.XPATH,
            "//div[contains(@class,'tcard active')]"
        )

        return self.wait.until(
            EC.visibility_of_element_located(active)
        ).text

    def get_current_selected_plan(self):
        return self.get_selected_plan().split("\n")[0]

    def click_next_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        ).click()

    def set_code(self, code):
        self.wait.until(
            EC.visibility_of_element_located(self.CODE_FIELD)
        ).send_keys(code)

    def click_confirm_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        ).click()

    def click_order_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)
        ).click()

    def get_phone(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PHONE_VALUE)
        ).text

    def confirm_phone(self):
        self.click_next_button()

        code = retrieve_phone_code(self.driver)

        self.set_code(code)

        self.click_confirm_button()


    def click_payment_method(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PAYMENT_METHOD
            )
        ).click()

    def click_add_card(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_CARD_BUTTON
            )
        ).click()

    def click_card_add_confirm(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_CARD_CONFIRM_BUTTON
            )
        ).click()

    def set_card_number(self, number):
        self.wait.until(
            EC.visibility_of_element_located(
                self.CARD_NUMBER_FIELD
            )
        ).send_keys(number)

    def set_card_code(self, code):
        field = self.wait.until(
            EC.visibility_of_element_located(
                self.CARD_CODE_FIELD
            )
        )

        field.send_keys(code)

        print("Código cartão preenchido:", field.get_attribute("value"))

        field.send_keys(Keys.TAB)


    def close_payment_popup(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CLOSE_PAYMENT_BUTTON
            )
        ).click()

