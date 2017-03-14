#-*- coding:utf-8-*-
import time,os
import logging

'''
    日志类
    '''
class Loggr(object):
    
    def __init__(self,filename):
        self.logger = logging.getLogger(u'日志输出:')
        self.logger.setLevel(logging.DEBUG)     #控制日志文件中记录级别 
        if not os.path.exists(u'日志'):
            os.makedirs(u'日志')
        else:
            pass
        fh = logging.FileHandler(u'日志\%s'%(filename))       #设置文件日志
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")#设置日志格式
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        
    def debug(self,message):
        self.logger.debug(message)
 
    def info(self,message):
        self.logger.info(message)
 
    def war(self,message):       
        self.logger.warn(message)
       
    def error(self,message):
        self.logger.error(message)
 
    def cri(self,message):
        self.logger.critical(message)
        
    def exception(self,message):
        self.logger.exception(message)


        