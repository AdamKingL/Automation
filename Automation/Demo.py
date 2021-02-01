# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()

browser.get("http://ics.chinasoftinc.com/SignOnServlet")
print ("浏览器最大化")
browser.maximize_window()  #将浏览器最大化显示
time.sleep(2)

##用户登陆

browser.find_element_by_name("userName").send_keys("105771")
browser.find_element_by_xpath("//input[@id='password']").click()
browser.find_element_by_xpath("//input[@id='password']").send_keys("likunqi19940815")
browser.find_element_by_xpath("//input[@class='button']").click()
time.sleep(2)

##考勤系统
browser.find_element_by_xpath("//a[@href='/pptemplate/default/spage/kqzq.html']").click()

windows = browser.window_handles
browser.switch_to.window(windows[-1])
##WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='kaoqin']"))).click()
browser.find_element_by_xpath("//a[@href='http://ics.chinasoftinc.com:8010/sso/toLoginYellow']").click()
##用户登出
##browser.find_element_by_xpath("//a[@href='/logout']").click()
##browser.quit()

