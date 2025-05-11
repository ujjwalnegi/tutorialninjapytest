from selenium.webdriver.common.by import By
from base_pages.ElementLocatorPage import ElementLocatorPage


class RegisterPage(ElementLocatorPage):

    def __init__(self,
                 driver):  # __init__ constructor will be called automatically when the object will be created for class
        super().__init__(driver)

    first_name = "firstname"
    last_name = "lastname"
    email_name = "email"
    telephone_name = "telephone"
    password_name = "password"
    confirm_name = "confirm"
    privacy_policy_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"

    def enter_firstname(self, firstname):
        self.enter_data(firstname,"first_name",self.first_name)
        # self.driver.find_element(By.NAME, self.first_name).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.enter_data(lastname,"last_name",self.last_name)
        # self.driver.find_element(By.NAME, self.first_name).send_keys(lastname)

    def enter_email(self, email):
        self.enter_data(email,"email_name",self.email_name)
        # self.driver.find_element(By.NAME, self.email_name).send_keys(email)

    def enter_telephone(self, number):
        self.enter_data(number,"telephone_name",self.telephone_name)
        # self.driver.find_element(By.NAME, self.telephone_name).send_keys(number)

    def enter_password(self, password):
        self.enter_data(password,"password_name",self.password_name)
        # self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def confirm_password(self, confirm_password):
        self.enter_data(confirm_password,"confirm_name",self.confirm_name)
        # self.driver.find_element(By.NAME, self.confirm_name).send_keys(confirm_password)

    def select_privacy_policy_checkbox(self):
        self.element_click("privacy_policy_name",self.privacy_policy_name)
        # self.driver.find_element(By.NAME, self.privacy_policy_name).click()

    def click_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        # self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
