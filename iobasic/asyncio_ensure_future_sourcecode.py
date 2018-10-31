#asyncio.ensure_future
#python3.5的新方法，
#asyncio_ensure_future_sourcecode.py源码分析
#转载自https://www.jianshu.com/p/e6244fc7934e

def ensure_future(coro_or_future, *, loop=None):
  
  # 把一个协程或者awaitable对象包装成期物(Future)
  if isinstance(coro_or_future, futures.Future):
      if loop is not None and loop is not coro_or_future._loop:
          raise ValueError('loop argument must agree with Future')
      # 直接返回
      return coro_or_future

  # 判断是否为生成器或协程包装器
  elif coroutines.iscoroutine(coro_or_future):
      if loop is None:
          loop = events.get_event_loop()
      # 创建 task 对象
      task = loop.create_task(coro_or_future)
      if task._source_traceback:
          del task._source_traceback[-1]
      return task
  
  # py 3.5下，判断对象是否为 awaitable 对象
  elif compat.PY35 and inspect.isawaitable(coro_or_future):
      return ensure_future(_wrap_awaitable(coro_or_future), loop=loop)
  else:
      raise TypeError('A Future, a coroutine or an awaitable is required')
