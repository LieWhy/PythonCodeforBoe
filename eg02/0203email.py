import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.boe.com.cn"  # 设置服务器
# mail_user = "ruanchaowei@boe.com.cn"  # 用户名
# mail_pass = "Boe12345"  # 口令

mail_user = "chenguixia@boe.com.cn"
mail_pass = "Boe12345"

sender = 'chenguixia@boe.com.cn'
receivers = ['ruanchaowei@boe.com.cn']  # 接收邮件

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')#邮件内容
message['From'] = Header('XXX', 'utf-8')
message['To'] = Header('RCW', 'utf-8')

subject = 'Python SMTP 邮件测试'        #邮件标题
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
