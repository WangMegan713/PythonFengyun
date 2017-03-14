# -*- coding:utf-8 -*-
#from element import Element
from appium import webdriver
class Operation:
    '''
    元素操作类
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def element_operat(self,operat,elements,keys):
        #operation = Operation()        
        if operat == u"点击":
            elements.click()
        elif operat == u"跳转":
            pass  
        elif operat == u"上滑":
            
        else: 
            elements.clear()
            elements.send_keys(keys) 
            
    #获取屏幕宽和高
    def getSize(self):
        x=self.driver.get_window_size()['width'] #获取手机屏幕宽度
        y=self.driver.get_window_size()['height']#获取手机屏幕高度
        return(x,y)
    
    #向左滑动
    def swipeLeft(self,t):
        l=self.getSize()
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.25)
        self.driver.swipe(x1,y1,x2,y1,t) #x1,y1：开始点想x,y坐标  x2,x2：结束点x,y坐标
        
    #向右滑动
    def swipeRight(self,t):
        l=self.getSize()
        x1=int(l[0]*0.25)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        self.driver.swipe(x1,y1,x2,y1,t)

    #向上滑动
    def swipeUp(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.75)
        y2=int(l[1]*0.25)
        self.driver.swipe(x1,y1,x1,y2,t)

    #向下滑动
    def swipeDown(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.25)
        y2=int(l[1]*0.75)
        self.driver.swipe(x1,y1,x1,y2,t)