#hello.py

'''
application()函数就是符合WSGI标准的一个HTTP处理函数，
它接收两个参数：
environ：一个包含所有HTTP请求信息的dict对象；
start_response：一个发送HTTP响应的函数。
'''
#实现web应用的wsgi处理函数
def application(environ, start_response):
	#start_response()函数接收两个参数，http响应码，一个list表示http header
	start_response('200 OK',[('Content-Type','text/html')])
	#将括号中的内容作为http响应的body发送给浏览器
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]