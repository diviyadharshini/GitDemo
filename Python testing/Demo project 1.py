import self as self
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.google.com/")
inputElems = driver.find_elements_by_css_selector('input[name=q]')
for inputElem in inputElems:
    inputElem.send_keys('selenium')
    inputElem.send_keys(Keys.ENTER)
driver.find_element_by_xpath("//a[@href='https://www.selenium.dev/']").click()
driver.find_element_by_xpath("//a[contains(text(),'Downloads')]").click()
driver.find_element_by_xpath("//div[@id='browsersExpand']").click()
driver.find_element_by_xpath("//body/div[@id='browsersContent']/p[5]/a[1]").click()
driver.find_element_by_xpath("//a[contains(text(),'ChromeDriver 86.0.4240.22')]").click()
print(driver.find_element_by_xpath("//td[contains(text(),'2020-09-03 19:26:47')]").text)
