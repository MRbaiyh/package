# w = 每个日期之间的间隔字符数
# l = 每周所占的行数
# c = 每个月之间的间隔字符数
import calendar
cal = calendar.calendar(2018)
print(cal)
import time
t = time.localtime()
print(t)
import timeit
def doit():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))

t1 = timeit.timeit(stmt=doit, number=10)
print(t1)
for i in range(10):
    print(i) 

#timeit 可以执行一个函数，来测量一个函数的执行时间