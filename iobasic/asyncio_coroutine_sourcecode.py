
#@asyncio.coroutine将一个生成器标记为协程

#asyncio_coroutine_sourcecode.py源码分析
#转载自https://www.jianshu.com/p/e6244fc7934e
def coroutine(func):
    # 将一个生成器标记为协程，如果在destroyed前没有调用，则会记录错误

    # 这个方法是使用 inspect.iscoroutinefunction 方法判断是否为协程方法，使用 types.coroutine 装饰的生成器，或 async def 语法定义的函数都会返回 True
    if _inspect_iscoroutinefunction(func):
        return func

    # 使用 co_flags 判断是否为生成器
    if inspect.isgeneratorfunction(func):
        coro = func
    else:
        @functools.wraps(func)
        def coro(*args, **kw):
            res = func(*args, **kw)
            
            # 判断 res 是否为期物，生成器 或 协程包装类 实例
            if isinstance(res, futures.Future) or inspect.isgenerator(res) or \
                    isinstance(res, CoroWrapper):
                res = yield from res

            elif _AwaitableABC is not None:
                # py 3.5 才会有 Awaitable 类
                try:
                    # 如果有 __await__属性，__await__属性只会返回一个不是协程的迭代器
                    await_meth = res.__await__
                except AttributeError:
                    pass
                else:
                    # 如果是 Awaitable 对象
                    if isinstance(res, _AwaitableABC):
                        # 使用 yield from 处理其迭代器
                        res = yield from await_meth()
            return res

    # 使用 types.coroutine 包装 coro(注意，多层 @types.coroutine 装饰不会影响,会直接return装饰的值)
    if not _DEBUG:
        if _types_coroutine is None:
            wrapper = coro
        else:
            wrapper = _types_coroutine(coro)
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwds):
          
            # 使用协程包装器处理
            w = CoroWrapper(coro(*args, **kwds), func=func)
            if w._source_traceback:
                del w._source_traceback[-1]
            # 如果是 py 3.5 则包装增加 协程 对象的属性，否则包装为 生成器 对象的属性
            w.__name__ = getattr(func, '__name__', None)
            w.__qualname__ = getattr(func, '__qualname__', None)
            return w
    
    # 用以别处使用 asyncio.iscoroutinefunction() 判断为 True 的作用
    wrapper._is_coroutine = True  # For iscoroutinefunction().
    return wrapper