import time

from selenium import webdriver
from config.chrome_options import options
from page_object.login_page import LoginPage
import allure


@allure.feature('登录模块测试')
class TestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome(options=options())

    def teardown_class(self):
        self.driver.quit()

    @allure.story('用户登录')
    @allure.title("cookie登录")
    def test_login_with_cookie(self):
        """
        用例描述：cookie登录
        """
        lp = LoginPage(self.driver)
        lp.login_with_cookie()
        time.sleep(3)

    @allure.story('用户登录故事2')
    @allure.title("异常测试")
    def test_exception(self):
        """
        用例描述：异常测试
        """
        with allure.step("测试开始"):
            pass
        i = 1 / 0
