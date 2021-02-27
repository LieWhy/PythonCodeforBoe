import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendBoeMail:
    receivers = ['ruanchaowei@boe.com.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    sender = 'chenguixia@boe.com.cn'  # 发送邮件
    mail_pass = "Boe12345"  # 口令
    mail_user = "chenguixia@boe.com.cn"  # 用户名
    mail_host = "smtp.boe.com.cn"  # 设置服务器


