# negilib/core.py
import time

def negilib(func):
    def wrapper(*a, **kw):
        s = time.perf_counter()
        r = func(*a, **kw)
        t = (time.perf_counter() - s) * 1000
        print(f"[negilib] {func.__name__}: {t:.3f} ms")
        return r
    return wrapper