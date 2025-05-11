from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self,
                 driver):  # __init__ constructor will be called automatically when the object will be created for class
        self.driver = driver

    my_account_xpath = "//h2[normalize-space()='My Account']"

    def validate_my_account_text(self):
        return self.driver.find_element(By.XPATH,self.my_account_xpath).is_displayed()