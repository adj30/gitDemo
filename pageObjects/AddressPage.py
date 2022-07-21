from selenium.webdriver.common.by import By


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    location_search_box = (By.ID, "country")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CLASS_NAME, "btn-success")
    success_text = (By.CLASS_NAME, "alert-success")
    india_text = (By.LINK_TEXT, "India")

    def get_location_search_box(self):
        return self.driver.find_element(*AddressPage.location_search_box)

    def get_checkbox(self):
        return self.driver.find_element(*AddressPage.checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*AddressPage.purchase_button)

    def get_success_text(self):
        return self.driver.find_element(*AddressPage.success_text)

    def click_text_india(self):
        return self.driver.find_element(*AddressPage.india_text).click()
