
#decorator2.py

#三层嵌套定义的函数，可以传入参数，并返回函数
#装饰器，即一个接受函数，返回函数的高级函数
#如果decorator需要传入参数，需要编写一个返回decorator的高阶函数：

'''
#关于参数的传递：
*args：输入数据长度不确定，通过*args将任意长度的参数传递给函数，系统
自动将任意长度参数用list表示。
**kargs：输入数据长度不确定，系统自动将任意长度参数用dict（字典）表示
'''

#定义传入参数，返回decorator的高阶函数
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator




#调用装饰器修饰函数now()的语法,并对text传入参数'execute'
@log('execute')
def now():
	print('2015-3-25')
#相当于执行newfunc()=log(now()),然后再执行原来的now()

now()#调用装饰后的now()函数

'''
newfunc()=log('execute')(now)
1）首先执行log('execute'),log(text)函数返回的是decorator（func),
2）于是，newfunc()变成newfunc2()=decorator(now),并且参数text是'execute'
3）然后，将函数now作为参数传递给decorator，decorator函数先执行打印语句
然后再返回 func(*args, **kw),
4)此时，原始的now()函数依然存在，因此调用now()，打印日期

'''
print(now.__name__)
#发现执行装饰之后函数对象的名字属性发生了变化，所以为了能够克服这点，需要将
#原始函数的属性如__name__放到wrapper()中，import functools完成，具体参见
#decorator3.py