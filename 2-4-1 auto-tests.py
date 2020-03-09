# some aspects of auto-tests

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)
button = browser.find_element_by_class_name("btn")
button.click()

message = browser.find_element_by_id("verify_message").text

assert "successful" in message