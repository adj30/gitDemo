import time

import pytest

from TestData.HomePageData import HomepageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.getlogger()
        home_page = HomePage(self.driver)

        home_page.get_name().send_keys(get_data["firstName"])
        log.info("First Name is :- " + get_data["firstName"])

        home_page.get_email().send_keys(get_data["email"])
        log.info("Email is :- " + get_data["email"])

        home_page.get_password().send_keys(get_data["password"])
        home_page.get_checkbox().click()

        self.select_option_by_text(home_page.get_gender(), get_data["gender"])
        log.info("Gender is :- " + get_data["gender"])

        home_page.get_submit_button().click()

        log.info("Success msg:- " + home_page.get_success_message().text)

        message = home_page.get_success_message().text
        assert "Success" in message
        # time.sleep(2)
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.getTestData("TestCase7"))
    def get_data(self, request):
        return request.param

    # @pytest.fixture(params=HomepageData.test_Homepage_data)
    # def get_data(self, request):
    #     return request.param
