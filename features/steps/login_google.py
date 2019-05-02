from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Access url Login')
def step(driver):
   driver.browser.get('http://www.google.com')

@given('Click button Sign In')
def step(driver):
   driver.browser.find_element_by_xpath("//a[@id='gb_70']").click()

@when('Fill Email')
def step(driver):
   driver.browser.find_element_by_xpath("//input[@id='identifierId']").send_keys('irwansyarifudin16@gmail.com')

@when('Click Button Next')
def step(driver):
   driver.browser.find_element_by_xpath("//span[contains(text(),'Berikutnya')]").click()
   element = WebDriverWait(driver.browser, 4).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))

@then('I should see element password')
def step(driver):
   driver.browser.find_element_by_xpath("//input[@name='password']")