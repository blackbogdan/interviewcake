__author__ = 'bkapusta'
from selenium import webdriver
#invoke the firefox browser
driver=webdriver.Chrome()
#navigate to the given weburl
driver.get("https://www.google.com")