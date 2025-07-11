# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from utilities import ReadConfigurations
#
#
# @pytest.fixture()
# def setup_and_teardown(request):
#     browser = ReadConfigurations.read_configuration("basic info", "browser")
#     if browser.__eq__("chrome"):
#         driver = webdriver.Chrome()
#     elif browser.__eq__("firefox"):
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Edge()
#     driver.maximize_window()
#     app_url = ReadConfigurations.read_configuration("basic info","url")
#     driver.get(app_url)
#     request.cls.driver = driver #this assigns driver to class
#     yield
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    app_url = ReadConfigurations.read_configuration("basic info", "url")

    if browser.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser.lower() == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
