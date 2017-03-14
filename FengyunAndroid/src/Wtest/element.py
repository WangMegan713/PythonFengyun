# -*- coding:utf-8 -*-
'''
定位元素类
'''
class Element(object):      
    #通过id定位元素
    def get_id(self,driver,id):
        element = driver.find_element_by_id(id)    
        return element
    #通过name定位元素
    def get_name(self,driver,name):
        element = driver.find_element_by_name(name)
        return element
    #通过classname定位元素
    def get_className(self,driver,className):
        element = driver.find_element_by_class_name(className) 
        return className  
    #通过xpath定位元素
    def get_xpath(self,driver,xpath):
        element = driver.find_element_by_xpath(xpath)
        return element
    #通过By定位元素
    def get_By(self,driver,how,what):
        element = driver.find_element(how,what)
        return element
    
    #根据用例判断调用定位元素的方式
    def get_elements(self,driver,locatMode,widgetValue):
        if locatMode == "name":     
            element = driver.find_element_by_name(widgetValue)
        elif locatMode == "xpath":
            element = driver.find_element_by_xpath(widgetValue)
        elif locatMode == "id":
            element = driver.find_element_by_id(widgetValue)
        elif locatMode == "switch":
            element = driver.switch_to.context(widgetValue)#跳转至H5页面
        else:
            element = driver.find_element_by_class_name(widgetValue)
        return element
            
            
            


    
    
    
