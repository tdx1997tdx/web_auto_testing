from page_object.login_page import LoginPage
from selenium import webdriver
from config.chrome_options import options

if __name__ == '__main__':
    driver = webdriver.Chrome(options)
    lp = LoginPage(driver)
    lp.login_with_cookie()
