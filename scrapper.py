from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = r'C:\WebScrapper\chromedriver.exe'
driver = webdriver.Chrome(PATH)

##Launch the website
driver.get("https://amazon.ca")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("camera")
search.send_keys(Keys.RETURN)

#sub_class = driver.find_element_by_class_name(r"a-size-medium a-color-base a-text-normal")
print(sub_class)



#time.sleep(5)
#print(driver.title)
#print(driver.page_source)

driver.quit()

