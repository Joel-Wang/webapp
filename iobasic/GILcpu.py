
#GILcpu.py

#CPU阻塞的多线程，这个容易电脑死机。。。。

import time
from threading import Thread
from datetime import datetime

def write(i):
	#打印现在时间
	print('{} start write --> {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
	l,sum_=list(range(50000000)),0
	for i in l:
		sum_ +=i
	print('{} end write --> {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))

def fun():
	print('start ...')
	for i in range(3):
		Thread(target=write,args=(i,),daemon=False).start()
	print('end ... ')

fun()
#输出结果，如果是10^8效果会很明显，即cpu阻塞后用thread效果不好，
#但那样电脑容易死机。。。。

'''
start ...
2018-10-31 15:43:54 start write --> 0
2018-10-31 15:43:55 start write --> 1
2018-10-31 15:43:56 start write --> 2
end ...
2018-10-31 15:44:02 end write --> 49999999
2018-10-31 15:44:03 end write --> 49999999
2018-10-31 15:44:03 end write --> 49999999
'''