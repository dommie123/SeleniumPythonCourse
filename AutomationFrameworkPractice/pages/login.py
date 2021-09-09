class LoginPage: 

    def __init__(self, driver):
        self.driver = driver

        self.username_text_id = "txtUsername"
        self.password_text_id = "txtPassword"
        self.login_btn_id = "btnLogin"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_text_id).clear()
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)
    
    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_id).click()