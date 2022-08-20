from selenium.webdriver import Keys

from config.config import url as index_url


class BasePage:

    # 构造函数
    def __int__(self, driver):
        self.driver = driver

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    def visit_index(self):
        self.driver.get(index_url)

    # 元素定位
    def locate(self, loc):
        return self.driver.find_element(*loc)

    # 输入文本
    def input(self, loc, text):
        self.locate(loc).send_keys(text)

    # 单击
    def click(self, loc):
        self.locate(loc).click()

    # refresh
    def refresh_page(self):
        self.driver.refresh()

    # 按下回车键
    def enter(self, loc):
        self.locate(loc).send_keys(Keys.ENTER)
