from selenium import webdriver


def openBrowser():

    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    browser = webdriver.Chrome(chrome_options=option)
    return browser
