from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class IndexPage(BasePage):
    uri = "/"
    # 核心元素
    search_input = (By.XPATH, '//*[@id="layout"]/div/div[1]/div[2]/div/span/div[1]/span/span[1]/input')

    def __init__(self, driver):
        super().__int__(driver)

    # 核心业务流

    def search(self, txt):
        self.visit_index()
        self.input(self.search_input, txt)
        self.enter(self.search_input)
