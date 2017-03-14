# -*- coding:utf-8 -*-
import xlrd,xlwt
from xlutils.copy import copy
import os,time
import zipfile

class ExcelData:
    '''
    表格操作类
    '''
    #获取自动化测试用例表格
    def open_excel(self,filename): 
        data = xlrd.open_workbook(os.path.join(os.getcwd(),filename))
        table = data.sheet_by_index(0)     #读取excel并读取第一页的用例
        return table
    #获取单个功能用例条数
    def get_nrows(self,table):
        nrows = table.nrows
        return nrows
    #获取用例编号
    def get_caseID(self,table,nrows):
        caseID = []
        for i in range(0,nrows):
           if table.cell(i,2).value == 'Y': 
               caseID.append(table.cell(i,0).value)
        return caseID
    #获取用例名称
    def get_caseName(self,table,nrows):
        caseName = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                caseName.append(table.cell(i,1).value)
        return caseName
    #获取是否执行用例标识
    def get_ifExcute(self,table,nrows):
        ifExcute = []
        for i in range(0,nrows):
            ifExcute.append(table.cell(i,2).value)
        return ifExcute
    #获取前置用例
    def get_preCase(self,table,nrows):
        preCase = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                preCase.append(table.cell(i,3).value)
        return preCase     
    #获取模块编号
    def get_modeNum(self,table,nrows):
        modeNum = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y': 
                modeNum.append(table.cell(i,4).value)
        return modeNum
    #获取测试步骤
    def get_stepName(self,table,nrows):
       stepName = []
       for i in range(0,nrows):
           if table.cell(i,2).value == 'Y':
               stepName.append(table.cell(i,5).value)
       return stepName
    #获取操作类型
    def get_actionType(self,table,nrows):
        actionType = []
        for i in range(0,nrows): 
            if table.cell(i,2).value == 'Y':          
                actionType.append(table.cell(i,6).value)
        return actionType
    #获取定位方式
    def get_locatMode(self,table,nrows):  
        widgetType = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                widgetType.append(table.cell(i,7).value)
        return widgetType
    #获取控件元素值
    def get_widgetValue(self,table,nrows):
        widgetValue = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                widgetValue.append(table.cell(i,8).value)
        return widgetValue
    #获取输入值
    def get_inputValue(self,table,nrows):
        inputValue = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                if (isinstance(table.cell(i,9).value,float)):
                    inputValue.append(str(int(table.cell(i,9).value)))
                else:
                    inputValue.append(table.cell(i,9).value)
        return inputValue
    #获取断言方法
    def get_assertMethod(self,table,nrows):
        assertMethod = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                assertMethod.append(table.cell(i,10).value)
        return assertMethod
        
    #获取检查点
    def get_checkPoint(self,table,nrows):
        checkPoint = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                checkPoint.append(table.cell(i,11).value)
        return checkPoint
    
    #获取断言失败提示信息
    def get_failMsg(self,table,nrows):
        failMsg = []
        for i in range(0,nrows):
            if table.cell(i,2).value == 'Y':
                failMsg.append(table.cell(i,12).value)
        return failMsg
    
    
    #设置样式
    def set_style(self,name,height,bold=False):
        style = xlwt.XFStyle() # 初始化样式 
        font = xlwt.Font() # 为样式创建字体 
        font.name = name # 'Times New Roman' 
        font.bold = bold  #字体加粗
        font.color_index = 4
        font.height = height 
        style.alignment.horz = xlwt.Alignment.HORZ_CENTER 
        style.font = font  
        return style
    #写测试报告
    def write_excel(self,num,caseID,caseName,stepName,result,exception,startTime,endTime):
        excel = ExcelData()
        file = xlwt.Workbook()#创建工作簿
        curTime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
        sheet = file.add_sheet(u'蜂云电话Andriod测试报告',cell_overwrite_ok=True) #创建sheet 第二参数用于确认同一个cell单元是否可以重设值
        case_style = xlwt.XFStyle()
        case_font = xlwt.Font()      
        first_col = sheet.col(0)  #第一列 用例编号
        secon_col = sheet.col(1)  #第二列 用例名称
        third_col = sheet.col(2)  #第三列 测试步骤
        fourth_col = sheet.col(3) #第四列 测试结果
        fivth_col = sheet.col(4)  #第五列 异常信息      
        first_col.width=256*18
        secon_col.width=256*20 
        third_col.width=256*20 
        fourth_col.width=256*10
        fivth_col.width=256*80
        row0 = [u'用例编号',u'用例名称',u'测试步骤',u'测试结果',u'异常信息']
        row7 = [u'用例总数',u'通过数(Passed)',u'失败数(Failed)',u'总用时']
        for i in range(0,len(row0)):
            sheet.write(10,i,row0[i],excel.set_style('Times New Roman',220,True))
        for i in range(0,len(row7)):
            sheet.write(7,i,row7[i])
        sheet.write_merge(0,2,0,4,u'自动化测试报告详情',excel.set_style('Times New Roman',440,True))
        sheet.write(4,0,u'开始时间')
        sheet.write(5,0,u'结束时间')
        sheet.write(4,1,startTime)
        sheet.write(5,1,endTime)
        pass_count = 0
        for i in range(0,num):
            sheet.write(i+11,0,caseID[i])
            sheet.write(i+11,1,caseName[i])
            sheet.write(i+11,2,stepName[i])
            sheet.write(i+11,3,result[i])
            strExcept = str(exception[i])
            sheet.write(i+11,4,strExcept)
            if result[i] == 'Passed':
                pass_count+=1
        fail_count = num-pass_count
        sheet.write(8,0,num)  #写入用例总数
        sheet.write(8,1,pass_count) #写入通过用例数
        sheet.write(8,2,fail_count) #写入失败用例数
        if not os.path.exists(u'测试报告'):
            os.makedirs(u'测试报告')
        else:
            pass
        file.save(u'测试报告\%s.xls'%(curTime))
        


 
        
        
        
        
        
        