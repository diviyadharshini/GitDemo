from selenium import webdriver
'''validateText ="Option2"'''
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
'''driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()'''
driver.find_element_by_css_selector("#name").send_keys("Option2")
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()