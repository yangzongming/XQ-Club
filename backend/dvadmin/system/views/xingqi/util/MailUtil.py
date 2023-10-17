# -*- coding: utf-8 -*-
from email.mime.application import MIMEApplication
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header



def send_email(mail, filename):
    mail_host = "smtp.126.com"
    mail_user = "lao_yang_cool@126.com"
    mail_pass = "KVLXBNGMJSQSJBPT"

    sender = 'lao_yang_cool@126.com'
    receivers = [ mail + '@xingqikeji.com']

    message = MIMEMultipart()
    message['From'] = Header(u'请购单','utf-8')
    message['To'] =  Header(u'测试','utf-8')

    att1 = MIMEApplication(open(filename, 'rb').read())
    att1["Content-Type"] = 'application/octet-stream'
    att1.add_header('Content-Disposition', 'attachment',
                    filename=("系统报价" + '.xlsx'))
    message.attach(att1)

    subject = u"系统报价----"
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("mail send sucessfull")
    except smtplib.SMTPException:
        print("mail send error")