from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Testone(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.click_on_shop_menu()
        products = checkout_page.get_product_titles()

        log.info("getting all product titles")
        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            log.info(product_name)
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                break

        confirm_page = checkout_page.click_checkout_button()
        address_page = confirm_page.click_checkout_button()
        log.info("Entering country name as India")
        address_page.get_location_search_box().send_keys("ind")

        self.verify_link_presence("India")
        address_page.click_text_india()
        address_page.get_checkbox().click()
        address_page.get_purchase_button().click()

        success_text = address_page.get_success_text().text
        log.info(f"Text received from application is {success_text}")
        assert "Success! Thank you!" in success_text
