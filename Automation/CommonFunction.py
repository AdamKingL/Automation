# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import GlobalParam

browser = GlobalParam.GL_browser
flag = "" ##TRUE 表示3天以内，包含3天；FALSE 表示3天以上

# 通用函数
class Compare():
    #def __init__(self):
    # 判断申请时长是否小于等于3天
    def is_Lower3Days(self, Duration):
        if str(Duration)[0:2] == "1天" or str(Duration)[0:2] == "2天":
            flag = "TRUE" 
        elif str(Duration)[0:2] == "3天":
            if str(Duration)[:] == "3天":
                flag = "TRUE"
            else:
                flag = "FALSE"
        else:
            if str(Duration)[1:3] == "小时" or str(Duration)[2:4] == "分钟":
                flag = "TRUE"
            else:
                flag = "FALSE"
        return flag


class Data():
    #def __init__(self):
    #读取电子流信息
    def ReadData(self,dataType):
        if dataType == "公出申请" :
            processData = []
            processData.append(dataType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##公出地点
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##公出时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##公出说明
            processData.append("")
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=5]/div[position()=1]/div/div").text)  ##流水号

        elif dataType == "年假申请" :
            processData = []
            processData.append(dataType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##请假时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##请假原因
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##扣减顺序
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=5]/div[position()=1]/div/div").text)  ##流水号
            
        elif dataType == "事假申请" :
            processData = []
            processData.append(dataType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##请假时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##请假原因
            processData.append("")
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##流水号
            
        elif dataType == "病假申请" :
            processData = []
            processData.append(dataType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##请假时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##请假原因
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##累计已休
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=5]/div[position()=1]/div/div").text)  ##流水号

        elif dataType == "补休申请" :
            processData = []
            processData.append(dataType)  ##请求类型
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=1]/div/div").text)  ##姓名
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=1]/div[position()=2]/div/div").text)  ##工号
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=2]/div/div").text)  ##开始日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=1]/div/div").text)  ##结束日期
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=3]/div[position()=2]/div/div").text)  ##请假时长
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=1]/div/div").text)  ##申请时间
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=2]/div[position()=1]/div/div").text)  ##请假原因
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=4]/div[position()=2]/div/div").text)  ##扣减顺序
            processData.append("")
            processData.append(browser.find_element_by_xpath("//div[@class='module_item' and position()=1]/.//div[@class='_frm_item' and position()=5]/div[position()=1]/div/div").text)  ##流水号
            
        else:
            processData = []
            print (dataType)

        return processData

class Process():
    #def __init__(self):
    #通过并提交给下一级审批
    def ApproveToNextLevel(self,NextLevelApproverID):
        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@class,'pms_pass')]")))
        browser.find_element_by_xpath("//input[contains(@class,'pms_pass')]").click()                               #点击 通过
        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='选择审批人']")))
        browser.find_element_by_xpath("//div[@class='btn' and text()='请选择']").click()                            #点击 请选择
        iframe=browser.find_element_by_xpath("//iframe[contains(@name,'layui-layer-iframe')]")
        browser.switch_to.frame(iframe);                                                                            #切换弹框
        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='info' and text()='全部审批人']")))
        browser.find_element_by_xpath("//div[@class='info' and text()='全部审批人']").click()                       #点击 全部审批人
        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='search_box']/.//input[@placeholder='请输入姓名、工号、手机号']")))
        browser.find_element_by_xpath("//div[@class='search_box']/.//input[@placeholder='请输入姓名、工号、手机号']").send_keys(NextLevelApproverID) #输入审批人
        browser.find_element_by_xpath("//div[@class='search_box']/div[@class='ser flex center horizontal_center']").click() #点击 搜索
        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='item_box']/div")))
        browser.find_element_by_xpath("//div[@class='item_box']/div").click()                                       #点击 审批人
        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'btn submit') and text()='确认']")))
        browser.find_element_by_xpath("//div[contains(@class,'btn submit') and text()='确认']").click()             #点击 确认
        browser.switch_to.default_content();                                                                        #切换到默认html
        browser.find_element_by_xpath("//div[contains(@class,'btn cancel') and text()='取消']").click()             #点击 取消
##        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'btn submit') and text()='确认']")))
##        browser.find_element_by_xpath("//div[contains(@class,'btn submit') and text()='确认']").click()             #点击 确认
        print("To DM")
        time.sleep(5)
            
    #直接通过
    def ApproveDirectly(self):
        WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@class,'pms_pass')]")))
##        browser.find_element_by_xpath("//input[contains(@class,'pms_pass')]").click()                               #点击 通过
        print("Approoved")
        time.sleep(5)
