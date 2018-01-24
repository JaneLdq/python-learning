import datetime
import functools

def log(text):
    def decorator(func):
        # 原始函数的__name__等属性复制到wrapper函数中, 否则得到的被包装过的now函数的__name__值会变成'wrapper'
        @functools.wraps(func)
        # (*args, **kw)使得wrapper()函数可以接受任意参数的调用
        def wrapper(*args, **kw):
            print("%s %s(): " % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 相当于调用 now = log('execute')(now)
@log('execute')
def now():
    print(datetime.datetime.now())

now()
