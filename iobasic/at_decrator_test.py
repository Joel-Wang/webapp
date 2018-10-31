#at_decrator_test

import time

def time(func):
    print(time.ctime())
    return func()

@time  # 从这里可以看出@time 等价于 time(xxx()),但是这种写法你得考虑python代码的执行顺序
def funcx():
    print('Hello world!')