#coroutine3.py
#本例来源https://blog.csdn.net/soonfly/article/details/78361819
#主要是为了debug摸清协程的执行与消息模型 的使用，尽力理解吧。。。
'''
基于asyncio.coroutine和yield from的协程调度
1）  asyncio是一个基于事件循环的实现异步I/O的模块。通过yield from，我们可以将协程
    asyncio.sleep的控制权交给事件循环，然后挂起当前协程；之后，由事件循环决定何
    时唤醒asyncio.sleep,接着向后执行代码。 
2）  协程之间的调度都是由事件循环决定。
'''


import asyncio,random
@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
#下面表达式详细理解参考https://blog.csdn.net/yjk13703623757/article/details/77918633/
if __name__ == '__main__':#当本.py文件运行时，以下的代码将被运行，否则不运行
    loop = asyncio.get_event_loop()#获取事件loop
    tasks = [
        smart_fib(10),
        stupid_fib(10),
    ]
    loop.run_until_complete(asyncio.wait(tasks))#loop消息循环运行事件
    print('All fib finished.')
    loop.close()#loop关闭

'''每次结果都不一样
Stupid one think 0.06154019309505601 secs to get 1
Smart one think 0.0733732739597368 secs to get 1
Smart one think 0.0406143121405062 secs to get 1
Stupid one think 0.11823223577780327 secs to get 1
Smart one think 0.12359590279048781 secs to get 2
Smart one think 0.19029565120277728 secs to get 3
Smart one think 0.0698830403453009 secs to get 5
Stupid one think 0.359326579165301 secs to get 2
Smart one think 0.1782595265796431 secs to get 8
Smart one think 0.11857297392716173 secs to get 13
Smart one think 0.07741036482366884 secs to get 21
Stupid one think 0.3981751936721468 secs to get 3
Smart one think 0.12766397850412023 secs to get 34
Smart one think 0.0018432779339677243 secs to get 55
Stupid one think 0.28174704994471544 secs to get 5
Stupid one think 0.3150829954095111 secs to get 8
Stupid one think 0.2526232784497487 secs to get 13
Stupid one think 0.36495551581704566 secs to get 21
Stupid one think 0.07726020263674319 secs to get 34
Stupid one think 0.2606526068813464 secs to get 55
All fib finished.
'''