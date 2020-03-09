# search in selenium
import time
from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Doston")

input2 = browser.find_element_by_name("last_name")
input2.send_keys("Matyakubov")

inout3 = browser.find_element_by_class_name("city")
inout3.send_keys("Tashkent")

input4 = browser.find_element_by_id("country")
input4.send_keys("Uzbekistan")

submit_btn = browser.find_element_by_css_selector("button.btn")
submit_btn.click()

time.sleep(30)
browser.quit()