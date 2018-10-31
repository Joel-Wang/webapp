webbasic文件夹下程序及文件说明
	
	本文件夹的基本内容如下，基本分为小结5点

1)tcpbasic.py为基本网页访问获取信息功能

2)tcpsever.py为服务器程序，
tcpclient.py为客户端程序
先运行sever，再运行client，可能windows下多线程会出错，这可能跟系统的某些设置有关系，不过只要能建立单一线程，程序的功能基本就算实现了。

3)hello.html为编写简单网页，点击变成红色

4)wsgihello.py为使用wsgi编写的wsgi处理函数，在其中定义application
wsgisever.py为对应的服务器的程序，在其中importwsgihello,并调用application
启动sever然后按照要求访问，运行后浏览器输入http://localhost:8000/看结果

5）使用web框架flask编写web app
pip安装flask，anaconda可以忽略不计

6）使用mvc模式基于flask，通过调用html模板编写web app
cmd运行flaskmvc.py启动web服务器，flask自带5000监听，所以通信什么的都不用管，home.html为首页模板，form.html为登录页面模板，signin-ok.html为登录成功页面模板，3个模板放在与flaskmvc.py的web app程序同一级的文件夹templates目录下

小结：

	1）需要了解tcp，IP基本知识，知道如何使用tcp编写服务器程序和客户端
	2）网页html的结构与编写
	3）wsgi如何编写web app，服务器处理函数
	4）使用flask编写 web app
	5）MVC 模式框架编写web app
