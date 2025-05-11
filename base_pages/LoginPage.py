from selenium.webdriver.common.by import By
from base_pages.ElementLocatorPage import ElementLocatorPage


class LoginPage(ElementLocatorPage):
    def __init__(self,driver):  # __init__ constructor will be called automatically when the object will be created for class
        super().__init__(driver)

    email_xpath = "//input[@name='email']"
    password_id = "input-password"
    login_xpath = "//input[@value='Login']"
    error_msg_xpath = "//div[contains(text(),'Warning: No match for E-Mail Address and/or Passwo')]"

    def enter_valid_email(self, valid_email):
        self.enter_data(valid_email,"email_xpath",self.email_xpath)
        # self.driver.find_element(By.XPATH, self.email_xpath).send_keys(valid_email)

    def enter_password(self,password):
        self.enter_data(password,"password_id",self.password_id)
        # self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def click_login_button(self):
        self.element_click("login_xpath",self.login_xpath)
        # self.driver.find_element(By.XPATH,self.login_xpath).click()

    def enter_invalid_email(self,invalid_email):
        self.enter_data(invalid_email,"email_xpath",self.email_xpath)
        # self.driver.find_element(By.XPATH, self.email_xpath).send_keys(invalid_email)

    def error_message_for_invalid_login(self):
        return self.driver.find_element(By.XPATH,self.error_msg_xpath).text

    def valid_login(self,valid_email,password):
        self.enter_valid_email(valid_email)
        self.enter_password(password)
        self.click_login_button()

    def invalid_login(self,invalid_email,password):
        self.enter_invalid_email(invalid_email)
        self.enter_password(password)
        self.click_login_button()


