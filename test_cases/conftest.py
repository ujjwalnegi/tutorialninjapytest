import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    request.cls.driver = driver #this assigns driver to class
    yield
    driver.quit()
