import psutil
import time
from Function.boe_weixin_notice import boe_weixin_notice

try:
    while True:
        mail = boe_weixin_notice()
        mem = psutil.virtual_memory()
        if mem[2] > 50:
            connect = mem[2]
            mail.sendmessage("10286172", "Monitoring", "内存使用超过%d" % connect)
        time.sleep(6)
except ValueError:
    print('获取值失败')
