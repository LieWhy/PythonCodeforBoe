import time

from Function.boe_weixin_notice import boe_weixin_notice

while True:
    time.sleep(1800)
    mail = boe_weixin_notice()
    mail.sendmessage('10286172', 'Click', '中国地质大学')
