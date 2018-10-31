# server.py
#简单web应用程序
'''
Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有
输入信息都可以通过environ获得，HTTP响应的输出都可以
通过start_response()加上函数返回值作为Body。
'''
#运行后浏览器输入http://localhost:8000/看结果

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入自己编写的application函数:
from wsgihello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()