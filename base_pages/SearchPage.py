from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self,driver): #__init__ constructor will be called automatically when the object will be created for class
        self.driver = driver

    valid_product_link_text = "HP LP3065"
    invalid_product_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"

    def validate_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_product_link_text).is_displayed()

    def validate_invalid_product(self):
        return self.driver.find_element(By.XPATH,self.invalid_product_xpath).is_displayed()


