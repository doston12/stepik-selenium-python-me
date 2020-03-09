import time

# webdriver to manipulate with browser
from selenium import webdriver

# initialize browser driver. literally, it says I'm gonna open a chrome browser
driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')

time.sleep(2)

# method get is used to open a page/url/link in browser
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(2)

# scroll down the page
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)

# find element in the page which has css type textarea
textarea = driver.find_element_by_css_selector(".textarea")

# write something in input field
textarea.send_keys("get()")
time.sleep(5)

# find the button submit
submit_button = driver.find_element_by_css_selector(".submit-submission")

# click the button
submit_button.click()
time.sleep(5)

# close the browser
driver.quit()