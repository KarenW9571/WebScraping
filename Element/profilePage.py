from selenium.webdriver.common.by import By
from .Base_Element import BaseElement
from .Base_Page import BasePage
from .Locators import Locator


class profilePage(BasePage):

    @property
    def playTime(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > ng-include > div > div > div.game-header-body > div.game-header-gameplay.hidden-game-header-collapsed > gameplay-module > div > div > ul > li:nth-child(2) > div.gameplay-item-primary > span'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def player(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > ng-include > div > div > div.game-header-body > div.game-header-gameplay.hidden-game-header-collapsed > gameplay-module > div > div > ul > li:nth-child(1) > div.gameplay-item-primary'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def rating(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > ng-include > div > div > div.game-header-body > div.game-header-title-container > div > div.game-header-title-rating > overall-rating > div > div > a > span.ng-binding'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def officialSite(self):
        xpath = '//*[@id="mainbody"]/div/div[1]/div[1]/div[2]/ng-include/div/div/ui-view/ui-view/div[1]/overview-module/description-module/div/div[2]/div/div[3]/div[2]/div[1]/official-links-module/div/div[2]/ul/li/div[2]/span[2]/a[1]'
        locator = Locator(by=By.XPATH, value=xpath)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def statButton(self):
        xpath = '//*[@id="primary_tabs"]/ul/li[7]/a'
        locator = Locator(by=By.XPATH, value=xpath)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def extButton(self):
        xpath = '//*[@id="primary_tabs"]/ul/li[9]/a'
        locator = Locator(by=By.XPATH, value=xpath)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def wishlist(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > div > ui-view > ui-view > div > div > div.panel-body > div > div:nth-child(3) > div:nth-child(2) > div.panel-body > ul > li:nth-child(5) > div.outline-item-description > a'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def secRank(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > div > ui-view > ui-view > div > div > div.panel-body > div > div:nth-child(3) > div:nth-child(2) > div.panel-body > ul > li:nth-child(5) > div.outline-item-description > a'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def secRankNum(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > div > ui-view > ui-view > div > div > div.panel-body > div > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(2) > div.outline-item-description > a'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def thdRank(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > div > ui-view > ui-view > div > div > div.panel-body > div > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(3) > div.outline-item-title.ng-binding'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def thdRankNum(self):
        selector = '#mainbody > div > div.global-body-content.pending.ready > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > div > ui-view > ui-view > div > div > div.panel-body > div > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(3) > div.outline-item-description > a'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def extList(self):
        selector = '//*[@id="mainbody"]/div/div[1]/div[1]/div[2]/ng-include/div/div/ui-view/ui-view/div/linked-items-module/div/div[2]/ul/li[1]/div/div[2]/div/div[1]/div[1]/a'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )

    @property
    def backBtn(self):
        selector = '//*[@id="mainbody"]/div/div[1]/div[1]/div[2]/ng-include/div/div/ui-view/ui-view/div/linked-items-module/div/div[2]/ul/li[1]/div/div[2]/div/div[1]/div[1]/a'
        locator = Locator(by=By.CSS_SELECTOR, value=selector)
        return BaseElement(
            browser=self.browser,
            locator=locator
        )
