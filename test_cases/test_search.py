import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.HomePage import HomePage
from base_pages.SearchPage import SearchPage
from test_cases.BaseTest import BaseTest


# @pytest.mark.usefixtures("setup_and_teardown")
class TestSearch(BaseTest):

    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_product("HP")
        assert search_page.validate_valid_product()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_product("sefreg")
        assert search_page.validate_invalid_product()
