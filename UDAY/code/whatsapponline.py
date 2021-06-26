from selenium import webdriver

import time
# Replace below path with the absolute path
browser = webdriver.Chrome(executable_path='/Tools/chromedriver_win32/chromedriver.exe')

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
time.sleep(20)
log_in = browser.find_element_by_xpath('//*[@title="New chat"]')
log_in.click()
search_bar = browser.find_elements_by_xpath('//*[@class="RPX_m"]')
search_bar.send_keys("swoji A")
time.sleep(3)
