#coroutine4.py
#本例来源https://blog.csdn.net/soonfly/article/details/78361819
#python3.5以后
#主要是为了debug摸清协程的执行与消息模型 的使用，主要是把coroutine3.py变成新的写法
'''
基于async和await的协程调度
Python3.5中引入的async和await：可以将他们理解成asyncio.coroutine/yield from的完
美替身。当然，从Python设计的角度来说，async/await让协程表面上独立于生成器而存在，将
细节都隐藏于asyncio模块之下，语法更清晰明了。 
'''
import time,asyncio,random
#定义一个协程coroutine
async def mygen(alist):
	while len(alist)>0:
		c=random.randint(0,len(alist)-1)
		print(alist.pop(c))
		await asyncio.sleep(1)
#定义两个list列表
strlist=["ss","dd","gg"]
intlist=[1,2,5,6]
#生成两个协程对象
c1=mygen(strlist)
c2=mygen(intlist)
print(c1)

#定义在当前文件中执行事件循环，用来调度协程
if __name__=='__main__':
	loop=asyncio.get_event_loop()#loop获取
	tasks=[
	c1,
	c2
	]
	loop.run_until_complete(asyncio.wait(tasks))#loop同时处理两个协程对象
	print('ALL fib finished.')
	loop.close()#loop关掉





'''
#一段单独运行的代码
import time,asyncio,random

#将一个函数通过async变为一个协程。
async def mygen(alist):
	while len(alist)>0:
		c=randint(0,len(alist)-1)
		#由于无法将generator转换为协程，因此下面是print
		print(alist.pop(c))
a=["aa","bb","cc"]
c=mygen(a)
print(c)
#输出：
'''
