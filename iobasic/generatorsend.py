
#generatorsend.py
'''函数send(msg):
其实next()和send()在一定意义上作用是相似的，区别是
send()可以传递yield表达式的值进去，而next()不能传
递特定的值，只能传递None进去。因此，我们可以看做
c.next() 和 c.send(None) 作用是一样的。
'''
'''
#send()函数执行时，send（None）为从头部执行，且第一
#次只能传递None。send(None)执行时从函数头部开始，到
#yield关键字返回后面的对象r，并且不执行yield对应的
#赋值语句之后send(n)可以传递值，每次调用send(n),传
#递一个参数n给生成器函数，并且从yield语句开始执行，
#并将n赋值给yield左边等号前面的变量，到下一次执行到
#yield结束，并且不执行yield的赋值操作，但返回yield
#后面的对象
'''
'''
总结：
第一次执行到yield r,只执行右半边，相当于 return r
第二次调用send(n)，执行左半边，相当于将n赋值，即n1=n
'''

def consumer():
	r='here'
	while True:
		n1=yield r
		if not n1:
			return
		print('[CONSUMER] Consuming %s... ' % n1)
		r='200 OK'+str(n1)

def produce(c):
    aa=c.send(None)
    print(aa)
    n=0
    while n<5:
    	n=n+1
    	print('[PRODUCER] Producing %s...' % n)
    	r1=c.send(n)
    	print('[PRODUCER] Consumer return: %s' % r1)
    c.close()

c=consumer()
produce(c)