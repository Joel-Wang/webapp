#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#服务器程序
#客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序

import socket
import threading
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#预先指定端口
s.bind(('127.0.0.1',9999))#9999为非标准服务，小于1024为标准服务需要管理员权限

#监听端口
s.listen(5)
print('waiting for connection....')


def tcplink(sock,addr):
	print('accept new connection from %s:%s...' % addr)
	sock.send(b'welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
		sock.close()
		print('connection from %s:%s closed.' % addr)

#定义一个永久循环来接受来自客户端的链接，accept()会等待并返回一个客户端的连接
while True:
	#接受一个新连接,单词意思：s                                                                                                       ocket(端口)，address（地址）
	sock,addr=s.accept()
	#创建新的线程来处理TCP连接
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()