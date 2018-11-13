#a = input("请输入内容：")
#print(a)
'''
def myf1():
    def myf2():
        print("lolllll")
        return 3
    return myf2

f = myf1()
print(type(f))
f()
'''
#fs = []
#for i in range(1,4):
    #fs.append(i)
#print(fs)

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())

import time
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper
        
@printTime
def hello():
    print("Hello world")
hello()

def hello3():
    print("我是手动执行的")

hello3 = printTime(hello3)
hello3()

f = printTime(hello3)
f()