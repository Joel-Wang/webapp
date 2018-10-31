
#generatoryieldf2.py

import logging

def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
f=fib(6)
'''
fab不是一个普通函数，而是一个生成器。因此fab(5)并没有执行函数，而是返回一个
生成器对象(生成器一定是迭代器iterator，迭代器一定是可迭代对象iterable) 
'''

def f_wrapper(fun_iterable):
	print('start')
	#yield from后面必须跟iterable对象(可以是生成器，迭代器)
	#所以可以用yield调用生成器并返回
	yield from fun_iterable
	print('end')
wrap=f_wrapper(fib(6))
for i in wrap:
	print(i,end=' ')

'''
结果：
start
1 1 2 3 5 8 end
'''