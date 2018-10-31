
#GILsleep.py
#睡眠阻塞的多线程

import time
from threading import Thread
from datetime import datetime

def write(i):
	#打印现在时间
	print('{} start write --> {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
	time.sleep(4)
	print('{} end write --> {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))

def fun():
	print('start ...')
	for i in range(3):
		Thread(target=write,args=(i,),daemon=False).start()
	print('end ... ')

fun()
#输出结果

'''
start ...
2018-10-31 15:23:06 start write --> 0
2018-10-31 15:23:06 start write --> 1
2018-10-31 15:23:06 start write --> 2
end ...
2018-10-31 15:23:10 end write --> 0
2018-10-31 15:23:10 end write --> 1
2018-10-31 15:23:10 end write --> 2
'''