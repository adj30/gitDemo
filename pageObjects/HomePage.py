from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def click_on_shop_menu(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckoutPage(self.driver)
        return check_out_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.message)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)
