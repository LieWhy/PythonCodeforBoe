import smtplib
from email.mime.text import MIMEText
from email.header import Header

from Function.SendBoeMail import SendBoeMail

# 调用封装函数
flag = SendBoeMail()

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')  # 邮件内容
message['From'] = Header('监控', 'utf-8')
message['To'] = Header('Weir', 'utf-8')
subject = 'Alert Warning'  # 邮件标题
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(flag.mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(flag.mail_user, flag.mail_pass)
    smtpObj.sendmail(flag.sender, flag.receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
