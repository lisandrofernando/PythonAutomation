from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
print(driver.current_url())
driver.get('http://automationpractice.com/')
driver.close()

