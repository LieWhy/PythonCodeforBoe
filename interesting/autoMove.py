'''
  实现思路： 1、获取鼠标位置
            2、如果鼠标超过3小时没有移动，利用random()随机出一个坐标
            3、当前坐标，移动到随机的坐标上
'''

import os, time
import random
import pyautogui
import traceback

print("=======================")
print("程序运行中请最小化界面")
print("=======================")

if __name__ == '__main__':

    # 一个死循环，会一直执行
    i = 1
    while i:
        try:
            # 鼠标执行移动命令前的间隔时间 (计划每3小时执行一次移动代码)单位（s）
            time.sleep(6)
            x = random.randint(0, 1600)
            y = random.randint(0, 900)

            # autoMove(x,y)
            # 鼠标移动到(a,b)坐标所用时间
            num_seconds = 1

            # 执行移动命令
            pyautogui.moveTo(x, y, duration=num_seconds)

            print("程序运行时长（小时）：", j)
            print("=======================")
        except:
            print(traceback.format_exc())
            continue
