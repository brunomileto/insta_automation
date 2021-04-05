from time import sleep
from selenium import webdriver


class LoginPage:
    def __init__(self, browser, *args, **kwargs):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')
        self.user_css_name = 'username'
        self.password_css_name = 'password'
    
    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector(f"input[name={self.user_css_name}]")
        password_input = self.browser.find_element_by_css_selector(f"input[name={self.password_css_name}]")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
    

browser = webdriver.Firefox(executable_path=r'C:\selenium_drivers\geckodriver.exe')
browser.implicitly_wait(5)

login_page = LoginPage(browser)
login_page.login("voutemarcar", "278666")

sleep(15)

browser.close()



def test_login_page(browser):
    login_page = LoginPage(browser)
    login_page.login("voutemarcar", "278666")

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0