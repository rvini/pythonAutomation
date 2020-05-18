from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser= webdriver.Chrome(executable_path="./chromedriver")
browser.set_window_size(900,900)
browser.get("https://www.youtube.com/")