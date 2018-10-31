#generatoryieldf1.py

#分析yield 与yield from功能不同的简单例子
'''
结果分析：
range(0, 5)这说明yield就是将range这个可迭代对象直接返回了。 
而yield from解析了range对象，将其中每一个item返回了。 
yield from iterable本质上等于for item in iterable: yield item的缩写版
即改为for item in range(5): yield item
'''

def g1():     
     yield  range(5)
def g2():
	#下面这两个句子注释一个，观察结果
    #yield  from range(5)
    for item in range(5): yield item

it1 = g1()
it2 = g2()
print('我是一')
for x in it1:
    print(x)
print()
print('我是二')
for x in it2:
    print(x)

'''
运行结果：
我是一
range(0, 5)

我是二
0
1
2
3
4
'''

