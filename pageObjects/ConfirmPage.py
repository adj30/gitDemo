from selenium.webdriver.common.by import By

from pageObjects.AddressPage import AddressPage


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def click_checkout_button(self):
        self.driver.find_element(*ConfirmPage.checkout_button).click()
        address_page = AddressPage(self.driver)
        return address_page
