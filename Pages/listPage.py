from selenium.webdriver.common.by import By
from WebScraping.Element.Base_Element import BaseElement
from WebScraping.Element.Base_Page import BasePage
import WebScraping.Element.Locators


class listPage(BasePage):

    url = 'https://boardgamegeek.com/browse/boardgame'

    @property
    def gameProfile(self, rank):
        xpath = '//*[@id="results_objectname' + str(rank) + '"]/a'
        locator = Locator(by=By.XPATH, value=xpath)
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
