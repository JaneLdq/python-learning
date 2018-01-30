import threading

# 可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Jane',), name="Thread A")
t2 = threading.Thread(target=process_thread, args=('jerry',), name="Thread B")

t1.start()
t2.start()

t1.join()
t2.join()
