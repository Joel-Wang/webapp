#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging;logging.basicConfig(level=logging.INFO)
#basicConfig为基本设置，INFO为消息级别
import asyncio,os,json,time
#依次为异步io,操作系统，数据交换（字符串编码与解码），时间处理
from datetime import datetime
#datetime，也是处理时间的模块
from aiohttp import web

#制作响应函数
def index(request):
	return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

#async def为协程定义语句
async def init(loop):#web服务器初始化
	app=web.Application(loop=loop)#制作响应函数合集
	app.router.add_route(method='GET',path='/',handler=index)#把响应函数添加到响应函数集合
	srv=await loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000')#创建服务器(连接网址、端口，绑定handler)
	return srv

loop=asyncio.get_event_loop()#创建事件
loop.run_until_complete(init(loop))#运行
loop.run_forever()#服务器不关闭