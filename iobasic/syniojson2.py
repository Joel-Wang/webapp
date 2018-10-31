
#syniojson2.py
#使用JSON对象标准格式序列化class创建的对象
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

#创建类
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score

#初始化对象
s=Student('Bob',20,88)

#定义一个从对象实例到dict的转换函数
def student2dict(std):
	return{
	'name': std.name,
	'age': std.age,
	'score': std.score
	}


print(json.dumps(s,default=student2dict))#s为类实例，default为对的处理方法
#dumps的详细用法参见https://docs.python.org/3/library/json.html#json.dumps