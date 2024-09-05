from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com')
search_input = driver.find_element_by_name('q')
search_input.send_keys('cat')
search_input.submit()
search_input.quit()