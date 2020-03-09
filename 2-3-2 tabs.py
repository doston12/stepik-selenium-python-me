# working with browser windows(tabs)

from selenium import webdriver
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

troll_button = browser.find_element_by_class_name("trollface")
troll_button.click()

new_tab = browser.window_handles[1]
browser.switch_to.window(new_tab)

x = browser.find_element_by_id("input_value").text
ans = calc(int(x))

answer = browser.find_element_by_id("answer")
answer.send_keys(str(ans))

button = browser.find_element_by_class_name("btn")
button.click()

alert_ans = browser.switch_to.alert