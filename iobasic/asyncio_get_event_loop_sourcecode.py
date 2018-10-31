
#asyncio.get_event_loop

#asyncio_get_event_loop_sourcecode.py源码分析
#转载自https://www.jianshu.com/p/e6244fc7934e
# DefaultEventLoopPolicy = _UnixDefaultEventLoopPolicy

class _UnixDefaultEventLoopPolicy(events.BaseDefaultEventLoopPolicy):
# 事件循环且监听子进程
_loop_factory = _UnixSelectorEventLoop

def __init__(self):
  super().__init__()
  self._watcher = None

def _init_watcher(self):
  with events._lock:
      if self._watcher is None:  # pragma: no branch
          self._watcher = SafeChildWatcher()
          if isinstance(threading.current_thread(),
                        threading._MainThread):
              self._watcher.attach_loop(self._local._loop)

def set_event_loop(self, loop):
  # 如果子监听已经设置，那么在主线程中调用 .set_event_loop() 会在子监听中调用 .attach_loop(loop)
  super().set_event_loop(loop)

  if self._watcher is not None and \
      isinstance(threading.current_thread(), threading._MainThread):
      self._watcher.attach_loop(loop)

def get_child_watcher(self):
  """
  Get the watcher for child processes.
  If not yet set, a SafeChildWatcher object is automatically created.
  """
  if self._watcher is None:
      self._init_watcher()

  return self._watcher

def set_child_watcher(self, watcher):
  """Set the watcher for child processes."""

  assert watcher is None or isinstance(watcher, AbstractChildWatcher)

  if self._watcher is not None:
      self._watcher.close()

  self._watcher = watcher