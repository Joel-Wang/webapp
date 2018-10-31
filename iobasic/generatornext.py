
#generatornext.py

#.__next__()函数：
#每次执行函数开始到yield 关键字，并返回yield后面的对象

def consumer():
	r='here'
	for i in range(3):
		#我理解类似于一个return 和一次循环终止的结合
		#体，每次到yield该次函数执行结束，返回r值
		yield r
		r='200 OK'+str(i)

c=consumer()
'''''这是python3.x之前的版本，新版本为__next__()
n1=c.next()
n2=c.next()
n3=c.next()
'''
n1=c.__next__()
n2=c.__next__()
n3=c.__next__()
print(n1)
print(n2)
print(n3)