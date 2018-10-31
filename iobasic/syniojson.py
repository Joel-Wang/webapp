
#syniojson.py
#使用JSON对象标准格式序列化对象，JSON表示的对象就是标准的JavaScript语言的对象
'''
常用数据类型对应关系：
JSON类型			python数据类型
{}				dict
[]				list
"string"		str
1234.56			int或float
true/false		True/False
null			None

'''
#注意：JSON和pickle函数很像，但pickle为load,而JSON为loads

#序列化为JSON对象,存入dumpj.txt
import json
d=dict(name='Bob', age=20, score=88)
f=open('dumpj.txt','w')#创建或打开文件，以二进制

print(json.dumps(d))
f.write(json.dumps(d))##将d序列化json#并写入文件
f.close()#每一个open都要对应close，不然请用with open('路径') as f

#将JSON对象反序列化（从磁盘到内存并输出）
f = open('dumpj.txt', 'r')

l = json.loads(f.read())##读取文件内容#将json对象反序列化
print(l)
f.close()
