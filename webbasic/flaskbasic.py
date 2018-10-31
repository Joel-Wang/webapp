#! python3
# -*- coding: utf-8 -*-
#flask框架的web app程序
'''
GET /：首页，返回Home；
GET /signin：登录页，显示登录表单；
POST /signin：处理登录表单，显示登录结果。
同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
'''

from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_from():
	return  '''	<form action="/signin" method="post">
				<p><input name="username"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''

@app.route('/signin',methods=['POST'])
def signin():
	#需要从request对象读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello,admin!</h3>'

	return '<h3>Bad username or password.</h3>'

if __name__=="__main__":
	app.run()