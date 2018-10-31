#asyncio.wait
#python3.5的新方法，
#asyncio_wait_sourcecode.py源码分析
#转载自https://www.jianshu.com/p/e6244fc7934e

@coroutine
def wait(fs, *, loop=None, timeout=None, return_when=ALL_COMPLETED):
  """
  fs 参数是 futures 或者 coroutines 序列，且不能为空
  return two sets of Future: (done, pending).
  用法:
      done, pending = yield from asyncio.wait(fs)
  """
  if isinstance(fs, futures.Future) or coroutines.iscoroutine(fs):
      raise TypeError("expect a list of futures, not %s" % type(fs).__name__)
  if not fs:
      raise ValueError('Set of coroutines/Futures is empty.')
  if return_when not in (FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED):
      raise ValueError('Invalid return_when value: {}'.format(return_when))

  if loop is None:
      loop = events.get_event_loop()

  # 把 fs 中的参数转化为期物 future 对象的集合
  fs = {ensure_future(f, loop=loop) for f in set(fs)}

  return (yield from _wait(fs, timeout, return_when, loop))