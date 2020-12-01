from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.refresh()
driver.back()
print(driver.title)
print(driver.current_url)
driver.close()
