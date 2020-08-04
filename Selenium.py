from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("http://techwithtim.net")
print(driver.title)

search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

# print(driver.page_source)

time.sleep(8)
driver.close()