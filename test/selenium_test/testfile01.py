import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import os

# browser = webdriver.Chrome()
# url = 'https://www.baidu.com'
#
# browser.get(url)
# browser.maximize_window()
# browser.find_element_by_id('kw').clear()  #clear()　　 用于清除输入框的内容，比如百度输入框里默认有个“请输入关键字”的信息，再比如我们的登陆框一般默认会有“账号”“密码”这样的默认信息。clear可以帮助我们清除这些信息。
# time.sleep(2)
# browser.find_element_by_id('kw').send_keys('selenium') ##send_keys("XX") 　　用于在一个输入框里输入内容。
# time.sleep(2)
# browser.find_element_by_id('su').click()  ##click() 　　用于点击一个按钮。
# time.sleep(2)
# browser.quit()

# WebElement  另一些常用方法：
# · text  获取该元素的文本
# · submit  提交表单
# · get_attribute  获得属性值
# dirver = webdriver.Chrome()
# url = 'https://www.baidu.com'
# dirver.get(url)
# time.sleep(2)
# data = dirver.find_element_by_id('cp').text
# print(data)
# time.sleep(3)
# dirver.find_element_by_id('kw').send_keys('selenium')
# time.sleep(2)
# ##用submit()来进行操作
# dirver.find_element_by_id('su').submit() ##这里用submit 与click的效果一样
# time.sleep(2)
# dirver.quit()

# 多层框架或窗口的定位(用法基本相同)：  frame框架  window窗口
# switch_to_frame()
# switch_to_window()
# 智能等待：
# implicitly_wait()
# frame = webdriver.Chrome()
# file_path = 'file:////' + os.path.abspath('./frame.html')
# frame.get(file_path)
# time.sleep(2)
#
# frame.implicitly_wait(30)     ### 隐式地等待一个无素被发现或一个命令完成；这个方法每次会话只需要调用一次
# frame.switch_to_frame('f1')   #### 先找到到ifrome1（id = f1）
# frame.switch_to_frame('f2')   #### 再找到其下面的ifrome2(id =f2)
#
# frame.find_element_by_id('kw').send_keys('selenium')
# frame.find_element_by_id('su').click()
# time.sleep(3)
# frame.quit()

# 调用js方法
# execute_script(script, *args)
# 在当前窗口/框架 同步执行javaScript
# 脚本：JavaScript的执行。
# *参数：适用任何JavaScript脚本。
# 使用：
# driver.execute_script（‘document.title’）

# ds = webdriver.Chrome()
# url = 'https://mail.qq.com/'
# ds.get(url)
#
# #ds.maximize_window()
# time.sleep(3)
# # data = ds.find_element_by_class_name('login_pictures_txt').text
# # print(data)
# # time.sleep(2)
# # ds.find_element_by_link_text('基本版').clear()
# time.sleep(3)
# # ds.find_element_by_name('')
# ds.find_element_by_id('forgetpwd').click()
# # ds.find_element_by_class_name('login_button').click()
# print('111')
# # ds.find_element_by_class_name('switch_btn_focus').click()
# # time.sleep(2)
# # ds.find_element_by_class_name('switch_btn').click()
# # time.sleep(2)
# # ds.find_element_by_class_name('inputstyle').clear()
# # time.sleep(2)
# # # js = 'var q=document.getElementById(\'u\');q.style.border=\'1px solid red\';'
# # # ds.execute_script(js)
# # time.sleep(2)
# ds.quit()

# upload = webdriver.Chrome()
# file_path = 'file:////' + os.path.abspath('login.html')
# upload.get(file_path)
# time.sleep(2)
# upload.maximize_window()
# time.sleep(2)
# # upload.find_element_by_name('file').click()
# # time.sleep(2)
# upload.find_element_by_name('file').send_keys('C:\\Users\Administrator\Desktop\Doc1.docx') ##上传文件操作
# time.sleep(2)
# upload.quit()

# baiduyun = webdriver.Chrome()
# url = 'https://mail.163.com/'
# baiduyun.get(url)
# baiduyun.maximize_window()
# time.sleep(1)
# baiduyun.find_element_by_class_name('j-inputtext dlemail').send_keys('ewdfweds')
# baiduyun.find_element_by_name('email').send_keys('18515064317')
# baiduyun.find_element_by_name('password').send_keys('1991liu0423')
# baiduyun.find_element_by_id('dologin').click()
# time.sleep(2)


# xiala = webdriver.Chrome()
# file_path = 'file:////' + os.path.abspath('login.html')
# xiala.get(file_path)
# time.sleep(2)
# xiala.maximize_window()
# time.sleep(2)
# m = xiala.find_element_by_id('ShippingMethod')
# m.find_element_by_xpath("//option[@value='10.69']").click()
# time.sleep(3)
# # alert 处理 语法如下：
# # a.accept()  # 等同于点击“确认”或“OK”
# # a.dismiss()  # 等同于点击“取消”或“Cancel”
# # a.authenticate(username,password)  # 验证，针对需要身份验证的alert，目前还没有找到特别合适的示例页面
# # a.send_keys(keysToSend)  # 发送文本，对有提交需求的prompt框（上图3）
# # a.text  # 获取alert文本内容，对有信息显示的alert框
# xiala.find_element_by_id('alert').click()
# time.sleep(2)
# a = xiala.switch_to.alert
# print(a.text)
# a.accept()
# time.sleep(2)
# # confirm 处理
# # 点击确定
# xiala.find_element_by_id('confirm').click()
# time.sleep(2)
# b = xiala.switch_to.alert
# print(b.text)
# b.accept()
# time.sleep(2)
# # 点击 取消
# xiala.find_element_by_id('confirm').click()
# time.sleep(2)
# b = xiala.switch_to.alert
# b.dismiss()
# # prompt 类型
# # 点击确定
# xiala.find_element_by_id('prompt').click()
# time.sleep(2)
# c = xiala.switch_to.alert
# print(c.text)
# c.accept()
# time.sleep(2)
# # 点击 取消
# xiala.get(file_path)
# time.sleep(3)
# xiala.find_element_by_id('prompt').click()
# time.sleep(2)
# d = xiala.switch_to.alert
# d.dismiss()
# time.sleep(2)
# # 输入文字
# xiala.get(file_path)
# time.sleep(3)
# xiala.find_element_by_id('prompt').click()
# time.sleep(2)
# e = xiala.switch_to.alert
# e.send_keys('!!!!!!!!!!!!!wangsuping love deeply  liudongpo!! oh yesh!!')
# time.sleep(2)
# e.accept()
#
# time.sleep(2)
# xiala.quit()

# bdsercher = webdriver.Chrome()
# url = 'https://www.baidu.com/'
# bdsercher.get(url)
# bdsercher.maximize_window()
# # bdsercher.implicitly_wait(300)
# #定位设置位置，找到对应的js，设置 display：none  为 block ，让设置上的四个文字链接可见；
# time.sleep(2)
# el = bdsercher.find_element_by_css_selector('#u1>a.pf')  ## #为id id为u1的标签，下边的class名为 pf的a标签
# ActionChains(bdsercher).move_to_element(el).perform()
# bdsercher.implicitly_wait(3)
# bdsercher.find_element_by_link_text('搜索设置').click()
# # m = bdsercher.find_element_by_name('NR')
# # m.find_element_by_xpath("//option[@value='50']").click()
# # m = Select(bdsercher.find_element_by_id('nr'))
# # m.select_by_index(2)
# time.sleep(2)
# m = bdsercher.find_element_by_id('nr')
# Select(m).select_by_value("50")
# # 索引
# # m.select_by_value()
#
# bdsercher.find_element_by_css_selector('#gxszButton>a.prefpanelgo').click()
# time.sleep(2)
# bdsercher.switch_to.alert.accept()
# time.sleep(2)
# bdsercher.find_element_by_id('kw').send_keys('selenium')
# bdsercher.find_element_by_id('su').click()
# # ##鼠标悬停操作；
# # chain = ActionChains(bdsercher)
# # time.sleep(2)
# # implement = bdsercher.find_element_by_css_selector("#u1>a.pf") ## #为id id为u1的标签，下边的class名为 pf的a标签
# # chain.move_to_element(implement).perform()  ##鼠标悬停操作；
# # #进入搜索设置页
# # bdsercher.implicitly_wait(3)
# # bdsercher.find_element_by_css_selector("div.bdpfmenu>a.setpref").click() ##找到class名为bdpfmenu的div标签下边class='setpref'的a标签，并且点击
#
# # 将滚动条至于页面最底部
# time.sleep(3)
# js  = "var q=document.documentElement.scrollTop=10000"
# bdsercher.execute_script(js)
# # 将滚动条移动到页面的顶部
# time.sleep(3)
# js1 = "var q=document.documentElement.scrollTop=0"
# bdsercher.execute_script(js1)
#
# time.sleep(5)
# bdsercher.quit()

# driver = webdriver.Chrome()
# file_path = 'file:////' + os.path.abspath('login.html')
# driver.get(file_path)
# driver.maximize_window()
# time.sleep(2)
# js = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(2)
# driver.find_element_by_id('name').clear()
# driver.find_element_by_id('name').send_keys(u'我是谁')
# time.sleep(2)
# # tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
# driver.find_element_by_id('name').send_keys(Keys.TAB)
# time.sleep(2)
# driver.find_element_by_id('pwd').send_keys('900880880')
# time.sleep(2)
# driver.find_element_by_class_name('subBtn').send_keys(Keys.ENTER)
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.quit()
#
# driver = webdriver.Chrome()
# url = 'https://www.baidu.com/'
# driver.get(url)
# driver.maximize_window()
# time.sleep(2)
# cookies = driver.get_cookies()
# print("-----------", cookies)
# time.sleep(2)
# a = driver.find_element_by_id('kw')
# a.send_keys('selenium')
# time.sleep(2)
# a.send_keys(Keys.CONTROL, 'a')
# time.sleep(2)
# a.send_keys(Keys.CONTROL, 'x')
# time.sleep(2)
# a.send_keys(u'哈哈哈')
# driver.find_element_by_id('su').send_keys(Keys.ENTER)
# time.sleep(2)
# driver.quit()

# Cookies 用法
# driver = webdriver.Chrome()
# url = 'https://www.baidu.com/'
# driver.get(url)
# driver.maximize_window()
# time.sleep(2)
# cookie1 = driver.get_cookie('BAIDUID') # 只能根据cookies 的name 进行获取
# print('1233333', cookie1)
# driver.add_cookie({'name': '123455', 'value': '0908908900'})
# cookies = driver.get_cookies()
# print("-----------", cookies)
# for cookie in cookies :
#     print('========:', cookie['name'], cookie['value'])
# driver.delete_cookie('BD_UPN')
# cookies = driver.get_cookies()
# print("-----------", cookies)
# for cookie in cookies :
#     print('2@@@@@@@:', cookie['name'], cookie['value'])
# driver.delete_all_cookies()
# cookies = driver.get_cookies()
# print("-----------", cookies)
# for cookie in cookies :
#     print('2!!!!:', cookie['name'], cookie['value'])
# driver.quit()

# 博客园注册
# driver = webdriver.Chrome()
# driver.get('http://passport.cnblogs.com/login.aspx?')
# driver.maximize_window()
# time.sleep(2)
# # driver.find_element_by_id('input1').send_keys('18515064317')
# # driver.find_element_by_id('input2').send_keys('1991liu0423')
# # time.sleep(2)
# driver.find_element_by_link_text('立即注册').click()
# time.sleep(2)
# driver.find_element_by_id('Email').send_keys('18515064317123@163.com')
# driver.find_element_by_id('PhoneNum').send_keys('18515064317')
# driver.find_element_by_id('LoginName').send_keys(u'能否')
# driver.find_element_by_id('DisplayName').send_keys(u'能否')
# driver.find_element_by_id('Password').send_keys('1991liu0423@')
# driver.find_element_by_id('ConfirmPassword').send_keys('1991liu0423@')
# time.sleep(2)
# driver.find_element_by_id('submitBtn').click()
# time.sleep(2)
# # ac = ActionChains(driver.find_element_by_class_name('geetest_slider_button'))
# # ActionChains(ac).move_by_offset(121, 0)
# driver.find_element_by_class_name('geetest_refresh_1').click()
# time.sleep(2)
# driver.find_element_by_class_name('geetest_refresh_1').click()
# time.sleep(2)
# # driver.quit()

# driver = webdriver.Chrome()
# file_path  = 'file:////' + os.path.abspath('login.html')
# driver.get(file_path)
# js  = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# driver.find_element_by_id('name').send_keys('1233')
# driver.find_element_by_id('pwd').send_keys('1212333')
# time.sleep(2)
# driver.find_element_by_class_name('subBtn').click()
# time.sleep(2)
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print('------', cookie['name'], cookie['value'])
# driver.quit()



