#coroutine2.py

'''
此程序有点问题，等调试好了再说吧
1、Task 对象包含 协程(coro) 和协程调用时间2个属性；
2、Loop 对象使用堆承载多个 Task 对象，根据 Task 对象中最小调用时间去执行对应的 coro。如果 coro 没有迭代完，则将此 coro 生成新的 task，然后 push 到 Loop 对象的堆中。
'''
# 简单的调用示例，消息模型实现异步io
import asyncio

@asyncio.coroutine
def coro_fun():
    yield from range(10)

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [asyncio.ensure_future(coro_fun())]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
'''
记住三个概念：
1、协程(coroutine)
2、任务(Task)
3、事件循环(loop)

'''