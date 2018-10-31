#.run_until_complete

#asyncio_run_until_complete_sourcecode.py源码分析
#转载自https://www.jianshu.com/p/e6244fc7934e
# DefaultEventLoopPolicy = _UnixDefaultEventLoopPolicy
def run_until_complete(self, future):
      """ 
      1、参数为协程，使用asyncio.wait()值也是协程
      2、会将协程包装成期物
      3、运行直到期物状态为 done
      """

      # 检查 loop 是否 close
      self._check_closed()

      new_task = not isinstance(future, futures.Future)
      future = tasks.ensure_future(future, loop=self)
      if new_task:
          # An exception is raised if the future didn't complete, so there
          # is no need to log the "destroy pending task" message
          future._log_destroy_pending = False

      # 添加 done 回调
      future.add_done_callback(_run_until_complete_cb)
      try:
          self.run_forever()
      except:
          if new_task and future.done() and not future.cancelled():
              # The coroutine raised a BaseException. Consume the exception
              # to not log a warning, the caller doesn't have access to the
              # local task.
              future.exception()
          raise
      future.remove_done_callback(_run_until_complete_cb)
      if not future.done():
          raise RuntimeError('Event loop stopped before Future completed.')

      return future.result()