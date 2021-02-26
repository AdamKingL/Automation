# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import ExportExcel
import CommonFunction
import GlobalParam

RM_LoginID = GlobalParam.GL_RM_LoginID
RM_Password = GlobalParam.GL_RM_Password
DM_ApproverID = GlobalParam.GL_DM_ApproverID

browser = GlobalParam.GL_browser
browser.implicitly_wait(30)  #隐性等待，最长30秒（在此单独设置全局适用）

browser.get("http://ics.chinasoftinc.com/SignOnServlet")
##print ("浏览器最大化")
browser.maximize_window()  #将浏览器最大化显示

##用户登陆
browser.find_element_by_name("userName").send_keys(RM_LoginID)
browser.find_element_by_xpath("//input[@id='password']").click()
browser.find_element_by_xpath("//input[@id='password']").send_keys(RM_Password)
browser.find_element_by_xpath("//input[@class='button']").click()

##考勤系统
browser.find_element_by_xpath("//a[@href='/pptemplate/default/spage/kqzq.html']").click() #点击考勤系统

windows = browser.window_handles
browser.switch_to.window(windows[-1])
browser.find_element_by_xpath("//a[@href='http://ics.chinasoftinc.com:8010/sso/toLoginYellow']").click() #点击新考勤系统

windows = browser.window_handles
browser.switch_to.window(windows[-1])
browser.find_element_by_xpath("//div[@class='menulist_item']/div[contains(text(),'审批')]").click() #点击审批

##审批并读取数据到excel
time.sleep(1)
Result = browser.find_elements_by_xpath("//div[contains(text(),'暂无审批数据')]")
WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='page_number' and contains(text(),'未审批')]")))
print("有审批数据")
i = 1
j = 1
num = 0
if Result == [] :
    WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]")))
    processType = browser.find_element_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]").text
    while j == 1 :
        # 读取电子流信息
        processData = CommonFunction.Data().ReadData(dataType=processType)
        print(processType)
        
        # RM 审批
        if processType == "公出申请" :
            CommonFunction.Process().ApproveToNextLevel(NextLevelApproverID=DM_ApproverID)
            processData.append("通过 下一级DM审批")  # 审批状态
            print ("公出 需DM审批")
            
        elif processType == "年假申请" :
            CommonFunction.Process().ApproveDirectly()
            processData.append("通过")  # 审批状态
            print ("年假 RM直接审批")

        elif processType == "补签申请" :
            CommonFunction.Process().ApproveDirectly()
            processData.append("通过")  # 审批状态
            print ("补签 RM直接审批")
            
        elif processType in ["事假申请","病假申请","补休申请"]:
            requestDuration = processData[6]
            flag_isLower3Days = CommonFunction.Compare().is_Lower3Days(Duration=requestDuration)
            print (flag_isLower3Days)
            if flag_isLower3Days == "TRUE":
                CommonFunction.Process().ApproveDirectly()
                processData.append("通过")  # 审批状态
                print ("RM直接审批")
            else:
                CommonFunction.Process().ApproveToNextLevel(NextLevelApproverID=DM_ApproverID)
                processData.append("通过 下一级DM审批")  # 审批状态
                print ("需DM审批")
                
            
        # 写入excel
        if processType in ["公出申请","年假申请","事假申请","病假申请","补休申请","补签申请"]:
            ExportExcel.Write_Excel().add_to_excel(values=processData)
        else:
            i = i+1
            print ("不写入excel")
            
        ##循环控制
        num = num+1
        time.sleep(3)
        ele = browser.find_elements_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]")
        if ele != [] :
            browser.find_element_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]").click()
            processType = browser.find_element_by_xpath("//li[position()="+str(i)+"]/.//div[@class='info']/div[position()=1]").text
            j = 1
        else :
            j = 0

        print(num)

##用户登出
##browser.find_element_by_xpath("//a[@href='/logout']").click()
browser.quit()
