@given('Access url')
def step(context):
   driver.browser.get('http://www.google.com')

@when('we visit google')
def step(driver):
   driver.browser.find_element_by_xpath("//img[@id='hplogo']")

@then('it should have a title "Google"')
def step(driver):
   assert driver.browser.title == "Google2"