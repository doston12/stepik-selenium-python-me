# working with <select> tag - working with lists

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

x = browser.find_element_by_id("num1").text
y = browser.find_element_by_id("num2").text
ans = int(x) + int(y)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(str(ans))

button = browser.find_element_by_class_name("btn")
button.click()

