from selenium.webdriver.common.by import By

from base_pages.SearchPage import SearchPage
from base_pages.ElementLocatorPage import ElementLocatorPage


class HomePage(ElementLocatorPage):
    def __init__(self,
                 driver):  # __init__ constructor will be called automatically when the object will be created for class
        super().__init__(driver)

    search_box_field_xpath = "//input[@name='search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_xpath = "//a[@title='My Account']//i"
    login_xpath = "//a[normalize-space()='Login']"
    register_xpath = "//body//nav//div//div//ul//li//ul//li//a[normalize-space()='Register']"

    def enter_product_in_search_box(self, product_name):
        # search_box = self.driver.find_element(By.XPATH, self.search_box_field_xpath)
        # search_box.click()
        # search_box.clear()
        # search_box.send_keys(product_name)
        self.enter_data(product_name,"search_box_field_xpath",self.search_box_field_xpath)

    def click_search_button(self):
        self.element_click("search_button_xpath",self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account(self):
        self.element_click("my_account_xpath",self.my_account_xpath)
        # self.driver.find_element(By.XPATH,self.my_account_xpath).click()

    def select_login_option(self):
        self.element_click("login_xpath",self.login_xpath)
        # self.driver.find_element(By.XPATH,self.login_xpath).click()

    def select_register_option(self):
        self.element_click("register_xpath",self.register_xpath)
        # self.driver.find_element(By.XPATH,self.register_xpath).click()

    def search_product(self,product_name):
        self.enter_product_in_search_box(product_name)
        self.click_search_button()
        return SearchPage(self.driver)

    def login(self):
        self.click_on_my_account()
        self.select_login_option()

    def register(self):
        self.click_on_my_account()
        self.select_register_option()
