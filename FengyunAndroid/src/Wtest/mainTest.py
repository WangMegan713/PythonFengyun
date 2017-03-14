# -*- coding:utf-8 -*-
from excelData import ExcelData
from element import Element
from operation import Operation
from initDriver import Driver
from sendEmail import Email
from initDriver import Driver
from Log import Loggr
import time,os
from selenium.common.exceptions import NoSuchElementException

class testMain:
    logName = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))+'.log'
    element = Element()  #初始化Element
    operat = Operation()   #动作类型  
    excel = ExcelData()  #实例化excel对象，获取用例信息
    table = excel.open_excel(u'移动端功能自动化测试.xlsx') #打开测试用例表格
    nrows = excel.get_nrows(table)    #获取用例行数
    caseID = excel.get_caseID(table, nrows)#获取用例编号
    caseName = excel.get_caseName(table, nrows) #获取用例名称
    actionType = excel.get_actionType(table, nrows)#获取操作类型
    modeID = excel.get_modeNum(table, nrows) #获取模块编号
    stepName = excel.get_stepName(table, nrows) #获取步骤名称
    locatMode = excel.get_locatMode(table, nrows) #获取定位方式
    widgetValue = excel.get_widgetValue(table, nrows) #获取控件元素值
    inputValue = excel.get_inputValue(table, nrows) #获取输入值
    logger= Loggr(logName)     #log日志
    num = len(stepName) #用例条数
    e_time = [] #执行时间列表
    result = [] #结果列表
    errorData = [] #异常列表
    def doTest(self,beforeCount,lastNum):  
        print beforeCount
        driver1 = Driver()     #初始化驱动
        driver = driver1.get_driver()
        
        
        driver.implicitly_wait(8)   #隐式等待8s
        isLast = True            
        for i in range(lastNum,self.num):          
            try:
                time.sleep(3)
                self.element.get_id(driver,"com.phone580.cn.ZhongyuYun:id/iv_sign_success_close").click()#关闭每日签到弹框
            except:
                pass
            if self.modeID[i] == beforeCount:  #判断是否为同一个功能
                self.e_time.append(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                print self.locatMode[i],self.widgetValue[i],self.actionType[i], self.inputValue[i]
                if self.caseID[i]!='':
                    self.logger.info(u'用例编号：'+self.caseID[i]+u'\t'+u'用例名称：'+self.caseName[i]+u'\t'+u'测试步骤：'+self.stepName[i]) #将测试步骤写入log日志   
                else:
                    self.logger.info(u'测试步骤：'+self.stepName[i]) #将测试步骤写入log日志   
                try:
                    self.element.get_name(driver,"稍后再说").click()   #关闭升级弹框
                except:
                    pass                             
                try:
                    elements = self.element.get_elements(driver,self.locatMode[i],self.widgetValue[i]) #获取界面元素                        
                except NoSuchElementException,e: 
                    self.logger.exception(e)   #将异常信息写入log日志   
                    self.result.append('Failed')
                    self.errorData.append(e)
                else:
                    self.operat.element_operat(self.actionType[i], elements, self.inputValue[i])      #执行操作
                    self.result.append('Passed')
                    self.errorData.append(' ')
            if self.modeID[i] > beforeCount: #不同用例
                lastNum = i        
                print i
                beforeCount = self.modeID[i]
                isLast = False  
                driver1.quit_driver()    #退出驱动
                break           
        if isLast != True:     #用例未执行完毕时
            self.doTest(self,beforeCount,lastNum)  
        else:   
            endTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))               #用例执行完毕时           
            driver1.quit_driver()
            print self.result
            print self.errorData
            self.excel.write_excel(self.num, self.caseID, self.caseName, self.stepName, self.result, self.errorData,self.e_time[0],endTime)     
    
if __name__ == '__main__':  
    test = testMain()
    test.doTest(1,0)   
    test_email = Email()
    test_email.send_attachMail(u'自动化测试报告',u"测试报告详情见附件")

