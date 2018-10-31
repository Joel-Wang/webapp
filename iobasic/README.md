iobasic文件夹下的基本说明：
	可以先看最后的小结梳理。

1）	syniobasic.py 同步io实现基本的操作文件与目录的功能
	为同步读写情况下基本的io操作，可能会涉及到os模块，os.path，datatime模块，功能为获得当前目录下的文件目录，并按格式输出目录对应的信息。
2）	synioserialize.py 同步io实现序列化与反序列化,使用pickle模块，dumps(),load()函数
	序列化与反序列化基本操作，仅限于python内部（不同编程语言使用pickle
	可能会出错，因此要使用xml或json
3）	syniojson.py  将一个简单的dict对象转化为json
	syniojson2.py 从class实例转换为dict对象（student2dict函数实现），再转换为json对象
	使用JSON对象标准格式序列化class创建的对象

4)	generatorFibo.py生成器实现Fibonoci数列，每次调用fib(n)生成前n个

5）	generatornext.py生成器yield语句被__next__()调用的执行效果，
	yield格式，yield r
	第一次从函数头开始执行到yield r并返回r，之后每次从yield 开始执行直到再次遇见yield。

6）	generatorsend.py生成器yield语句被send(n)与send(None)调用的执行效果，
	yield格式，n1=yield r
	第一次send(None)从函数头开始执行到yield r并返回r，
	第二次及之后每次send(n),从yield 开始执行，只执行左边n1=n赋值，直到再次遇见yield，执行右半边yield r返回r。

7）	装饰器decorator：
	即一个接受函数，返回函数的高级函数，采用两层或三层嵌套函数，并使用@符号调用
	decorator1.py
	二层嵌套定义的函数，不可以传入参数，但可以返回函数
	decorator2.py
	三层嵌套定义的函数，可以传入参数，并返回函数
	decorator4.py
	一个应用装饰器的测试实例，不传入参数，但执行装饰器的函数之后返回函数本身，要正确执行原始函数，不能发生名字属性变化
	decorator5.py
	分析yield 与yield from功能不同的简单例子，yield from iterable本质上等于for item in iterable: yield item的缩写版，而yield 直接返回可迭代对象

8）	python的多线程：
	py3 解释器每执行 15ms 释放 GIL
	GIL 全局解释器锁：
	一个线程运行 Python，而其他 N 个睡眠或者等待 I/O。(保证同一时刻只有一个线程对共享资源进行存取)

	GILsleep.py 睡眠阻塞的多线程，对于睡眠操作或者 I/O 操作，多线程的作用非常明显，明显减少所消耗总时间；
	GILcpu.py   对于 CPU 计算型操作，多线程操作反而因为多线程间获取 GIL 而增加总的消耗时间。这个程序搞不好cpu就死了。。。

9）	python的异步编程思想：使用协程（coroutine)
	协程运行说明：
	coroutine.py
	与generatorsend.py相同,主要是为了描述python协程的实现。Donald Knuth：“子程序就是协程的一种特例。”
	coroutine2.py
	一个基于asyncio.coroutine/yield from的协程例子。
		1）asyncio.coroutine将一个生成器标记为协程,而yield from 调用一个生成器
		2）由于yield from调用了一个协程，因此当前循环会继续执行，不等待调用协程的结束，等到改协程结束后直接拿返回值。
		3）因此，yield from基于当前时间循环实现了异步IO,之后的结果先后取决于各个协程运行的时间，
	coroutine3.py
	一个基于asyncio.coroutine/yield from的另一个协程例子
	coroutine_hello.py
	一个协程程序最简单的例子

	coroutine4.py
	基于async/await的协程例子

小结：
	上面所提到的都是为了理解python asynio异步io，协程，事件循环的含义
	1）需要知道基本IO,基本的list，tuple，dict，set等
	2）需要知道生成器generator
	3）需要知道高阶函数，装饰器decorator
	4）需要知道多线程的基本知识，GIL锁机制，cpu阻塞，睡眠阻塞
	5）然后，要理解asyncio.coroutine/yield from，进而理解async/await，事件循环，程序的基本结构