import sys


class TailCallException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(func):
    def _wrapper(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_code == f.f_back.f_back.f_code:
            raise TailCallException(args, kwargs)

        else:
            while True:
                try:
                    return func(*args, **kwargs)
                except TailCallException as e:
                    args = e.args
                    kwargs = e.kwargs

    return _wrapper
