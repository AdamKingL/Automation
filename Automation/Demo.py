# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import ExportExcel

browser = webdriver.Chrome()

browser.get("http://ics.chinasoftinc.com/SignOnServlet")
##print ("浏览器最大化")
browser.maximize_window()  #将浏览器最大化显示
time.sleep(2)

##用户登陆

browser.find_element_by_name("userName").send_keys("141990")
browser.find_element_by_xpath("//input[@id='password']").click()
browser.find_element_by_xpath("//input[@id='password']").send_keys("Sn19900313")
browser.find_element_by_xpath("//input[@class='button']").click()
time.sleep(2)

##考勤系统
browser.find_element_by_xpath("//a[@href='/pptemplate/default/spage/kqzq.html']").click() #点击考勤系统

windows = browser.window_handles
browser.switch_to.window(windows[-1])
browser.find_element_by_xpath("//a[@href='http://ics.chinasoftinc.com:8010/sso/toLoginYellow']").click() #点击新考勤系统

time.sleep(3)

windows = browser.window_handles
browser.switch_to.window(windows[-1])
browser.find_element_by_xpath("//div[@class='menulist_item']/div[contains(text(),'审批')]").click() #点击审批

##读取数据到excel
##Result = WebDriverWait(browser,10).until(EC.visibility_of_any_elements_located((By.XPATH,"//div[text()='公出申请']")))
time.sleep(3)
Result = browser.find_elements_by_xpath("//div[text()='公出申请1']")
print (Result)
if Result != [] :
    values_1 = [1, "百度搜索", "百度-百度搜索", "https://www.baidu.com", "Selenium", "pass", "4"]
    values_2 = [2, "百度搜索", "百度-百度搜索", "https://www.baidu.com", "Python", "error", "5"]
    ExportExcel.Write_Excel().add_to_excel(values=values_1)
    ExportExcel.Write_Excel().add_to_excel(values=values_2)




##用户登出
##browser.find_element_by_xpath("//a[@href='/logout']").click()
##browser.quit()

