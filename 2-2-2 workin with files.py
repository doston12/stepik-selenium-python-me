# working with files

from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element_by_name("firstname").send_keys("Doston")
browser.find_element_by_name("lastname").send_keys("Matyakubov")
browser.find_element_by_name("email").send_keys("doston@azzimut.com")

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "hello.txt")
file_button = browser.find_element_by_id("file")
file_button.send_keys(file_path)

browser.find_element_by_class_name("btn").click()
