#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议

#建立连接
s.connect(('www.nwpu.edu.cn',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost:www.nwpu.edu.cn\r\nConnection:close\r\n\r\n')

#接收数据
buffer = []

while True:
	#每次接收最多1k
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break

data=b' '.join(buffer)

#关闭连接
s.close()

header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#把接收数据写入文件
with open('nwpu.html','wb') as f:
	f.write(html)