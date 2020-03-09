# learning to work with unique selectors part 2

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration1.html")

firstname = browser.find_element_by_css_selector(".first_block .first")
firstname.send_keys("Doston")

lastname = browser.find_element_by_css_selector(".first_block .second")
lastname.send_keys("Matyakubov")

email = browser.find_element_by_css_selector(".first_block .third")
email.send_keys("doston@azzimut.com")

submit_button = browser.find_element_by_css_selector("button.btn")
submit_button.click()

time.sleep(1)

welcome_text_elt = browser.find_elements_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered" == welcome_text