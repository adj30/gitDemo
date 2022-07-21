from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def get_product_titles(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def click_checkout_button(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

