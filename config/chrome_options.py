from selenium import webdriver


def options():
    # chrome浏览器的配置项，可以通过修改默认参数，改变默认启动的浏览器的形态
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')

    return options
