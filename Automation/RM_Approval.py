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
##105771 likunqi19940815
##141990 Sn19900313
browser.find_element_by_name("userName").send_keys("141990")
browser.find_element_by_xpath("//input[@id='password']").click()
browser.find_element_by_xpath("//input[@id='password']").send_keys("Sn19900313")
browser.find_element_by_xpath("//input[@class='button']").click()
time.sleep(5)

##考勤系统
browser.find_element_by_xpath("//a[@href='/pptemplate/default/spage/kqzq.html']").click() #点击考勤系统

windows = browser.window_handles
browser.switch_to.window(windows[-1])
browser.find_element_by_xpath("//a[@href='http://ics.chinasoftinc.com:8010/sso/toLoginYellow']").click() #点击新考勤系统

time.sleep(15)
##WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='menulist_item']/div[contains(text(),'审批')]")))

windows = browser.window_handles
browser.switch_to.window(windows[-1])
browser.find_element_by_xpath("//div[@class='menulist_item']/div[contains(text(),'审批')]").click() #点击审批

##读取数据到excel
time.sleep(15)
Result = browser.find_elements_by_xpath("//div[contains(text(),'暂无审批数据')]")
print (Result)

i = 1
j = 1
if Result == [] :
    processType = browser.find_element_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]").text
    print (processType)

    while j == 1 :
    ##公出请求
        if processType == '公出申请' :
            processData = []
            processData.append(processType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##公出地点
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##公出时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##公出说明
            processData.append('')
            processData.append('')
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=5]/div[position()=1]/div/div").text)  ##流水号

        elif processType == '年假申请' :
            processData = []
            processData.append(processType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append('')
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##请假时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##请假原因
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##扣减顺序
            processData.append('')
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=5]/div[position()=1]/div/div").text)  ##流水号
            
        elif processType == '事假申请' :
            processData = []
            processData.append(processType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append('')
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##请假时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##请假原因
            processData.append('')
            processData.append('')
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##流水号
            
        elif processType == '病假申请' :
            processData = []
            processData.append(processType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append('')
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##请假时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##请假原因
            processData.append('')
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##累计已休
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=5]/div[position()=1]/div/div").text)  ##流水号


        print (processData)      
##        ExportExcel.Write_Excel().add_to_excel(values=processData)

        requrstDuration = processData[6]

        ##判断3天以内
        if str(requrstDuration)[0:2] == '1天' or str(requrstDuration)[0:2] == '2天':
            print("3天以内")
        elif str(requrstDuration)[0:2] == '3天':
            if str(requrstDuration)[:] == '3天':
                print("3天以内")
            else:
                print("3天以上")
        else:
            if str(requrstDuration)[1:3] == '小时' or str(requrstDuration)[1:3] == '分钟':
                print("3天以内")
            else:
                print("3天以上")
        
        ##循环控制
        i = i+1
        ele = browser.find_elements_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]")
        print (ele)
        if ele != [] :
            browser.find_element_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]").click()
            processType = browser.find_element_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]").text
            j = 1
            print (processType)
            print (j)
        else :
            j = 0
            print (j)


##用户登出
##browser.find_element_by_xpath("//a[@href='/logout']").click()
##browser.quit()
