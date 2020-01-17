from bs4 import BeautifulSoup
from Web_Scraper.Element.Base_Element import BaseElement, BaseElements, SoupElement


class BasePage(object):

    url = None

    def __init__(self, browser):
        self.browser = browser

    def go(self):
        self.browser.get(self.url)

    def parse(self, element):

        result = element.get_attribute('innerHTML')
        soup = BeautifulSoup(result, 'lxml')
        return SoupElement(soup=soup)
