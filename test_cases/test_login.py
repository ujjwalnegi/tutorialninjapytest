import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.HomePage import HomePage
from base_pages.LoginPage import LoginPage
from base_pages.AccountPage import AccountPage
from test_cases.BaseTest import BaseTest
from utilities import ExcelUtils


# @pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(BaseTest):

    @pytest.mark.parametrize("valid_email,password",ExcelUtils.get_data_from_excel("ExcelFiles/tutorialninja.xlsx","LoginCred"))
    def test_login_with_valid_credentials(self,valid_email,password):
        home_page = HomePage(self.driver)
        home_page.login()
        login_page = LoginPage(self.driver)
        login_page.valid_login(valid_email,password)
        account_page = AccountPage(self.driver)
        assert account_page.validate_my_account_text()

    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.login()
        login_page = LoginPage(self.driver)
        login_page.invalid_login("flaweufh32@gmail.com","Test1234")
        # expected_text = "Warning: No match for E-Mail Address and/or Password."
        # assert login_page.error_message_for_invalid_login().__contains(expected_text)