from datetime import time, datetime
from random import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.HomePage import HomePage
from base_pages.RegisterPage import RegisterPage
from test_cases.BaseTest import BaseTest


# @pytest.mark.usefixtures("setup_and_teardown")
class TestRegister(BaseTest):
    driver = None

    def test_register(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("ujjwal2")
        register_page.enter_lastname("negi2")
        register_page.enter_email(self.generate_random_email())
        register_page.enter_telephone("3874792")
        register_page.enter_password("Test1234")
        register_page.confirm_password("Test1234")
        register_page.select_privacy_policy_checkbox()
        register_page.click_continue_button()

    # def generate_random_email(self):
    #     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    #     return "ujjwal" + time_stamp + "gmail.com"
