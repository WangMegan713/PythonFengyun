# -*- coding:utf-8 -*-
import ConfigParser
import os,os.path,datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import traceback
import logging

'''
    自动发送邮件
    '''
class Email: 
    cf = ConfigParser.ConfigParser()
    cf.read(os.path.join(os.getcwd(),'EmailConf.ini'))  
    smtpaddr = cf.get('email','smtpaddr') #邮件服务器地址
    fromaddr = cf.get('email','fromaddr') #发件人地址
    password = cf.get('email','password') #密码
    sender = cf.get('email','sender')   #发件人名称
    toaddr = cf.get('email','toaddr')  #收件人地址
    ccaddr = cf.get('email', 'ccaddr') #抄送人地址
    print smtpaddr
    if smtpaddr == 'smtp.qq.com':   #使用QQ邮箱发送邮件
        smtp = smtplib.SMTP_SSL(smtpaddr, 465)
    else:
        smtp = smtplib.SMTP()       #实例化SMTP
    
    
    #发送普通文本邮件
    def send_plainMail(self,subject,msg):  
        msgText = MIMEText(msg,'plain','utf-8')    #纯文本邮件
        msgText['Subject'] = Header(subject,'utf-8')
        msgText['From'] = self.fromaddr #发件人地址
        msgText['To'] = self.toaddr     #收件人地址
        msgText['Cc'] = self.ccaddr     #抄送地址
        
        try:
            self.smtp.connect(self.smtpaddr)      # 连接邮件服务器
            self.smtp.login(self.fromaddr,self.password)   #登录邮件服务器
        except:
            print 'failed'
        else: 
            try:    
                self.smtp.sendmail(self.fromaddr,self.toaddr.split(',')+self.ccaddr.split(','),msg.as_string())
                logging.info(u"邮件发送成功")
            except Exception,e:
                logging.error(u"邮件发送失败")
                print traceback.format_exc()  
            finally:  
                self.smtp.quit()  
    
    #发送带附件的邮件（发送最新测试报告）
    def send_attachMail(self,subject,msg):
        base_dir =u'测试报告\\'
        listdir = os.listdir(base_dir)
        listdir.sort(key=lambda fn: os.path.getmtime(base_dir+fn) if not os.path.isdir(base_dir+fn) else 0) 
        filename = listdir[-1] #最新测试报告
        print filename
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject#邮件标题
        msgRoot['From'] = self.fromaddr #发件人地址
        msgRoot['To'] = self.toaddr     #收件人地址
        msgRoot['Cc'] = self.ccaddr     #抄送地址
        msgText = MIMEText('%s'%msg,'html','utf-8')#文字信息将以html形式呈现
        msgRoot.attach(msgText)
        att = MIMEText(open(u'测试报告\%s'%filename, 'rb').read(), 'base64', 'utf-8')#添加附件  
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s"'%filename
        msgRoot.attach(att)
        try:
            self.smtp.connect(self.smtpaddr)      # 连接邮件服务器
            self.smtp.login(self.fromaddr,self.password)   #登录邮件服务器
        except:
            print "邮件服务器登录失败"#登录失败
            print traceback.format_exc()           
        else:
            try:
                self.smtp.sendmail(self.fromaddr, self.toaddr.split(',')+self.ccaddr.split(','), msgRoot.as_string())#发送邮件 
            except Exception,e:
                logging.error(u"邮件发送失败")
                print traceback.format_exc()  
            finally:  
                self.smtp.quit()  

        
        