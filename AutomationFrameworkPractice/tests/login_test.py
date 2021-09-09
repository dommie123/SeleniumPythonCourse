from selenium import webdriver
import pytest, allure, moment

from AutomationFrameworkPractice.pages.home import HomePage
from AutomationFrameworkPractice.pages.login import LoginPage
from AutomationFrameworkPractice.utils import utils

@pytest.mark.usefixtures('test_setup')
class TestLogin():

    def test_login(self):
        driver = self.driver
        loginPage = LoginPage(driver)

        loginPage.enter_username(utils.USERNAME)
        loginPage.enter_password(utils.PASSWORD)
        loginPage.click_login()
        
    def test_logout(self):
        try:
            driver = self.driver
            homePage = HomePage(driver)

            homePage.click_welcome()
            homePage.click_logout()
            assert driver.title == "abc"
        except AssertionError as error:
            print("An assertion error has occurred!")
            print(error)
            testName = utils.whoami()
            date = moment.now().strftime('%d-%m-%Y_%H-%M-%S')
            screenshot_name = f"{testName}_{date}"
            allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Dominick Wliey/git/selenium_python_course/AutomationFrameworkPractice/screenshots/" + screenshot_name + ".png")
            raise
        except:
            print("An exception occurred!")
            testName = utils.whoami()
            date = moment.now().strftime('%d-%m-%Y_%H-%M-%S')
            screenshot_name = f"{testName}_{date}"
            allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Dominick Wliey/git/selenium_python_course/AutomationFrameworkPractice/screenshots/" + screenshot_name + ".png")
            raise
        else:
            print("Nothing failed! Great!")

