import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()
url = 'http://172.16.149.213:7078/RSM/login'
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id('user').send_keys('admin')
driver.find_element_by_id('pwd').send_keys('111111')
driver.find_element_by_id('remember_me').click()
driver.find_element_by_id('login_btn').click()
driver.implicitly_wait(5)
driver.find_element_by_id('27').click()
time.sleep(1)
driver.switch_to.frame('page_frame')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="syn_region_btn"]').click()
# driver.find_element_by_xpath('//button[@class="l_btn_search"]').click()
driver.switch_to.alert.accept()


