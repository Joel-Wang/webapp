# -*- coding: utf-8 -*-
#synioserialize.py
#序列化与反序列化基本操作，仅限于python内部（不同编程语言使用pickle
#可能会出错，所以生成的txt直接打开可能会乱码，因此要使用xml或json

#将一个对象序列化（从内存到磁盘），并写入文件
import pickle
d=dict(name='Bob',age=20,score=88)
pickle.dumps(d)#对d序列化

f=open('dump.txt','wb')#创建或打开文件，以二进制
pickle.dump(d,f)#将d序列化并写入文件
f.close()#每一个open都要对应close，不然请用with open('路径') as f

#反序列化（从磁盘到内存并输出）
f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)
f.close()
