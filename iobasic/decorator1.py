
#decorator1.py

#二层嵌套定义的函数，不可以传入参数，但可以返回函数

#装饰器，即一个接受函数，返回函数的高级函数
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
'''
#关于参数的传递：
*args：输入数据长度不确定，通过*args将任意长度的参数传递给函数，系统
自动将任意长度参数用list表示。
**kargs：输入数据长度不确定，系统自动将任意长度参数用dict（字典）表示
'''



#调用装饰器修饰函数now()的语法,
@log
def now():
	print('2015-3-25')

'''
#相当于执行newfunc()=log(now()),然后再执行原来的now(),
#PS:个人觉得，之所以执行原来的now(),并不是因为decorator
#的特性，而是因为wrapper()的返回值是 func（*args,**kw)，
#所以原来的函数now()依然存在
'''