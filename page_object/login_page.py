from selenium.webdriver.common.by import By

from base_page.base_page import BasePage
from utils.cookie_tool import get_cookie_dict


class LoginPage(BasePage):
    uri = "/login"
    # 核心元素
    phone = (By.ID, "mobile_input")

    def __init__(self, driver):
        super().__int__(driver)

    # 核心业务流

    def login_with_cookie(self):
        self.visit_index()
        for i in get_cookie_dict():
            self.driver.add_cookie(i)
        self.visit_index()
