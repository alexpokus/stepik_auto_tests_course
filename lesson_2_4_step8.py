from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

btn = browser.find_element_by_css_selector("#book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
btn.click()

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
inp = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
inp.send_keys(y)

button2 = browser.find_element_by_css_selector("#solve")
button2.click()
print(browser.switch_to.alert.text)

