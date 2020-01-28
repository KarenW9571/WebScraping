from selenium.webdriver.common.by import By
from .Base_Element import BaseElement
from .Base_Page import BasePage
from .Locators import Locator


class listPage(BasePage):

    url = 'https://boardgamegeek.com/browse/boardgame'

    def gameProfileBtn(self, rank):
        xpath = '//*[@id="results_objectname' + str(rank) + '"]/a'
        locator = Locator(by=By.XPATH, value=xpath)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    def listPrice(self, rank):
        xpath = '/html/body/div[2]/main/div/div[1]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[' + str(
            rank + 1) + ']/td[7]/div/div/div[1]'
        locator = Locator(by=By.XPATH, value=xpath)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )
