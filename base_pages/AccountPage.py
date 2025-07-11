from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:
    def __init__(self,
                 driver):  # __init__ constructor will be called automatically when the object will be created for class
        self.driver = driver

    my_account_xpath = "//h2[normalize-space()='My Account']"

    def validate_my_account_text(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.my_account_xpath))
            )
            return element.is_displayed()
        except:
            return False

    # return self.driver.find_element(By.XPATH,self.my_account_xpath).is_displayed()
