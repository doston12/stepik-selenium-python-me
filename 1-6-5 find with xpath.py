# finding elements using xpath

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

first_name = browser.find_element_by_name("first_name")
first_name.send_keys("Doston")

last_name = browser.find_element_by_name("last_name")
last_name.send_keys("Matyakubov")

city = browser.find_element_by_class_name("city")
city.send_keys("Tashkent")

country = browser.find_element_by_id("country")
country.send_keys("Uzbekistan")

button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
button.click()
