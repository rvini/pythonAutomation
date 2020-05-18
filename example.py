from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.youtube.com/")
print(driver.current_url)
driver.find_elements_by_xpath("//*[@id='text']").click()




