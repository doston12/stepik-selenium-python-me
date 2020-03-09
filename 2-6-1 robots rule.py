# working with radion buttons in selenium

from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_id("input_value").text
ans = browser.find_element_by_id("answer")
ans.send_keys(calc(int(x)))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()

button = browser.find_element_by_class_name("btn")
button.click()

