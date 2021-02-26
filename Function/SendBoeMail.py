import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendBoeMail:
    def __boemail__(self):
        # x = SendBoeMail()
        # x.__smtp__("smtp.boe.com.cn", "ruanchaowei@boe.com.cn", "Boe12345")
        mail_host = "smtp.boe.com.cn"  # 设置服务器
        # mail_user = "ruanchaowei@boe.com.cn"  # 用户名
        # mail_pass = "Boe12345"  # 口令

        mail_user = "chenguixia@boe.com.cn"
        mail_pass = "Boe12345"

        sender = 'chenguixia@boe.com.cn'
        receivers = ['ruanchaowei@boe.com.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    def __message__(self):
        message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')  # 邮件内容
        message['From'] = Header('XXX', 'utf-8')
        message['To'] = Header('RCW', 'utf-8')

        subject = 'Python SMTP 邮件测试'  # 邮件标题
        message['Subject'] = Header(subject, 'utf-8')
