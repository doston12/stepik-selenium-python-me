# working with element attributes

from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

treasure_element = browser.find_element_by_id("treasure")
x = int(treasure_element.get_attribute("valuex"))

answer = browser.find_element_by_id("answer")
answer.send_keys(calc(x))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_xpath('//*[@id="robotsRule"]')
radiobutton.click()

button = browser.find_element_by_class_name("btn")
button.click()
