import pytest
from AutomationFrameworkPractice.utils import utils

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type the name of the browser you want to use. If we recognize it, or have the respective driver, the tests will be conducted in that browser.")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    #global driver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    # elif browser == "iexplore":
    #     driver = webdriver.IExplorer(executable_path="../drivers/IEDriverServer.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(utils.URL)
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
    print("Test completed!")