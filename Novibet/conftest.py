import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def initialize(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--start-maximized")

    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(10)

    driver.get("https://www.novibet.gr/stoixima")

    request.cls.driver = driver

    yield

    driver.close()
    driver.quit()
