
# -*- coding: utf-8 -*-
#decorator4.py一个应用装饰器的测试实例

import time, functools


def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		start=time.time()
		fn(*args,**kw)
		end=time.time()
		print('%s executed in %s ms' % (fn.__name__, end-start))
		return fn(*args,**kw)
	return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
#测试两个函数是否成功装饰并执行完成
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')