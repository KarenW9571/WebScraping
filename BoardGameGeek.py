from Element.browser import openBrowser
from Element.listPage import listPage
from Element.profilePage import profilePage


browser = openBrowser()

list_page = listPage(browser=browser)
list_page.go()

# for rank in (1, 2):
#    list_page.gameProfileBtn(rank=rank).click()
list_page.gameProfileBtn(rank=rank).click()
listPrice = list_page.listPrice(rank=rank)
prof_page = profilePage(browser=browser)
playtime = prof_page.playTime.text
player = prof_page.player.text
rating = prof_page.player.text
website = prof_page.officialSite.attribute(attr_name=href)
print(website)
wishlist = prof_page.wishlist.text
prof_page.statButton.click()


browser.close()
