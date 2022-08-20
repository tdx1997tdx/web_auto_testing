from selenium import webdriver
from config.chrome_options import options
from page_object.login_page import LoginPage
from page_object.index_page import IndexPage
import allure
import pytest
from utils.json_tool import load_json
from utils.log_tool import logger
import time


@allure.feature('搜索模块测试')
class TestSearch:

    def setup_class(self):
        self.driver = webdriver.Chrome(options=options())
        lp = LoginPage(self.driver)
        lp.login_with_cookie()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("test_input,story,title", load_json("./data/search_data.json"))
    def test_search(self, test_input, story, title):
        """
        用例描述：搜索测试
        """
        # 动态添加模块和标题
        allure.dynamic.story(story)
        allure.dynamic.title(title)
        ip = IndexPage(self.driver)
        ip.search(test_input["search_txt"])
        logger.info(str(test_input) + "finish")
        time.sleep(2)
