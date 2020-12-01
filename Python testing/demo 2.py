from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https:www.gmail.com")
driver.find_element_by_id("identifierId").send_keys("diviyadharshini123@gmail.com")
driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
