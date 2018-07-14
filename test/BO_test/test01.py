import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()
url = 'http://172.16.149.211:70/BO/login.jsp'
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('111111')
driver.find_element_by_id('captchaImage').click()
time.sleep(2)
driver.find_element_by_id('isRememberUsername').click()
driver.find_element_by_class_name('login_button').click()
# cookies = driver.get_cookies()
# print('jjjjjjjjjjj:', cookies)
# for cookie in cookies:
#     print('========:', cookie['name'], cookie['value'])
driver.implicitly_wait(5)
driver.find_element_by_class_name('ux-desktop-shortcut-text').click()
driver.find_element_by_id('tool-1079-toolEl').click()


