# working with alerts

from selenium import webdriver
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element_by_class_name("btn")
button.click()

alert = browser.switch_to.alert
alert.accept()

x = int(browser.find_element_by_id("input_value").text)
ans = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(str(ans))

button = browser.find_element_by_class_name("btn")
button.click()
