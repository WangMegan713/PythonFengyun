# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver

'''
    驱动类
    '''
class Driver:
    def __init__(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.4.4'
        desired_caps['deviceName']='fee3908c'
        desired_caps['appPackage']='com.phone580.cn.ZhongyuYun'
        desired_caps['appActivity']='com.phone580.cn.ZhongyuYun.ui.activity.EnterActivity'
       # desired_caps['appWaitActivity']='com.phone580.cn.ZhongyuYun.ui.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #返回driver，以便后期调用driver类获取
    def get_driver(self):
        return self.driver 
    def quit_driver(self):
        self.driver.quit()
    