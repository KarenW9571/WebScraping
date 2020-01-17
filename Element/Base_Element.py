from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from bs4 import BeautifulSoup


class BaseElement(object):
    def __init__(self, browser, locator):
        self.browser = browser
        self.locator = locator
        
        self.web_element = None
        self.find()


    def find(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None


    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None


    def attribute(self, attr_name):
        attr = self.web_element.get_attribute(attr_name)
        self.attr = attr
        return attr
    
    @property
    def text(self):
        text = self.web_element.text
        return text

class BaseElements(object):
    def __init__(self, browser, locator):
        self.browser = browser
        self.locator = locator

        self.lists = None
        self.getList()
  
    def getList(self):
        lists = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(locator=self.locator)
        )
        self.lists = lists 
        
        return lists 



class SoupElement(object): 

    def __init__(self, soup): 

        self.soup = soup

    def capture_element(self, element): 
        if element.next == 0: 
            if element.text == 1 : 
                element = self.soup.find_all(element.parserLoc[0], text = element.parserLoc[1])[element.num].text
                self.elementParsed = element
                return element
            else: 
                element = self.soup.find_all(element.parserLoc[0], class_ = element.parserLoc[1])[element.num].text
                return element
        elif element.next == 1: 
            if element.class_ == 1: 
                element = self.soup.find_all(element.parserLoc[0], text = element.parserLoc[1])[element.num].next_sibing
                self.elementParsed = element
                return element 
            else: 
                element = self.soup.find_all(element.parserLoc[0], class_ = element.parserLoc[1])[element.num].next_sibing
                return element 
    
    def capture_next_element(self,parserLoc):
        element = self.elementParsed.find_next(parserLoc.name)
        self.elementParsed = element
        return SoupElement(element)

    @property
    def text(self): 
        try:
            text = self.elementParsed.text
            return text 
        except: 
            return  'Unknown'