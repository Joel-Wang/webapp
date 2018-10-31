#! python3
# -*- coding: utf-8 -*-
#flask框架的web app程序,使用MVC模式编写，
'''
GET /：首页，返回Home；
GET /signin：登录页，显示登录表单；
POST /signin：处理登录表单，显示登录结果。
同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
'''
#导入框架
from flask import Flask
#request官方文档介绍对于 Web 应用，与客户端发送给服务器的数据
#交互至关重要。在 Flask 中由全局的 request 对象来提供这些信息
from flask import request
#render_template()函数来实现模板的渲染
from flask import render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_from():
	return  render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
	#需要从request对象读取表单内容：
	username=request.form['username']
	password=request.form['password']
	if username=='admin' and password=='password':
		return render_template('signin-ok.html',username=username)
		return render_template('form.html',message='Bad username or password',username=username)

if __name__=="__main__":
	app.run()