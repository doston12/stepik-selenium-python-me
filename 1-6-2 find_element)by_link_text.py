# finding link according to given text

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.degreesymbol.net/")
time.sleep(3)

# locating hyperlink text - match fully
#link = browser.find_element_by_link_text("» Degree symbol examples")

# locating hyperlink text - match partially
link = browser.find_element_by_partial_link_text("examples")

link.click()

time.sleep(5)
browser.quit()