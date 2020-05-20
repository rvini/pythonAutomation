from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://outlook.live.com/owa/")
driver.find_element_by_xpath("/html/body/header/div/aside/div/nav/ul/li[2]/a").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='i0116']").send_keys("vinitha.rajesh@outlook.com")
driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='i0118']").send_keys("to be replaced")
driver.find_element_by_xpath("//*[@id='idSIButton9']").click()