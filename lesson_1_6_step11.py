from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector("input:required.form-control.first")
    element1.send_keys("First")
    element2 = browser.find_element_by_css_selector("input:required.form-control.second")
    element2.send_keys("Second")
    element3 = browser.find_element_by_css_selector("input:required.form-control.third")
    element3.send_keys("Third")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
