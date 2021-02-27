import psutil
import time
from Function.boe_weixin_notice import boe_weixin_notice


def mem_info():
    mem = psutil.virtual_memory()
    info = {'mem_total': mem[0], 'mem_free': mem[1], 'mem_percent': mem[2], 'mem_used': mem[3]}
    return info


res = mem_info()


def main():
    m_men = res
    if m_men['men_percent'] > 50:
        connect = ('内存使用超过%d' % m_men)
        boe_weixin_notice.sendmessage("10286172", "Monitoring", connect)
    time.sleep(60)
