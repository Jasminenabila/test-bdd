from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def before_all(driver):

	driver.browser = webdriver.Chrome()

def after_all(driver):
	driver.browser.quit()