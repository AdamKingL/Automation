#GlobalParam.py 全局变量模块
from selenium import webdriver

GL_RM_LoginID = "141990"
GL_RM_Password = "Sn19900313"
GL_DM_ApproverID = "0000016073"

GL_DM_LoginID = "16073"
GL_DM_Password = "Jodie0418"
GL_GM_ApproverID = ""

GL_Name = "谢成志"

#有界面浏览器模式
GL_browser = webdriver.Chrome()

#无界面浏览器模式
##chrome_options = webdriver.ChromeOptions()
##chrome_options.add_argument('--headless')
##chrome_options.add_argument('--disable-gpu')
##
##GL_browser = webdriver.Chrome(chrome_options=chrome_options)
