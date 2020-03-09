
import math, time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

crypto = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element_by_partial_link_text(crypto)
link.click()

first_name = browser.find_element_by_name("first_name")
first_name.send_keys("Doston")

last_name = browser.find_element_by_name("last_name")
last_name.send_keys("Matyakubov")

city = browser.find_element_by_class_name("city")
city.send_keys("Tashkent")

country = browser.find_element_by_id("country")
country.send_keys("Uzbekistan")

submit_button = browser.find_element_by_tag_name("button")
submit_button.click()

