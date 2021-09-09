from selenium import webdriver
import pytest

class TestSkip():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/Dominick Wliey/git/selenium_python_course/drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()

        yield
        driver.close()
        driver.quit()
        print("Test completed!")
    
    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
    
    @pytest.mark.skip(reason="This test is pointless. Why was it even included in the first place? LOL!")
    def test_skip_me(self):
        assert True

    @pytest.mark.windows
    def test_windows(self):
        assert "Windows" == "Windows"

    @pytest.mark.mac
    def test_mac(self):
        assert "Macintosh" == "Macintosh"