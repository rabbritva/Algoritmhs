from time import time

def time_test(func, *args, **kwargs):
    ts = time()
    func(*args,**kwargs)
    te = time()
    print(f"Function {func.__name__} finished work for {te-ts:.3f} seconds\n")