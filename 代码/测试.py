import time
import _thread
def loopl():
    print('start loopl at :', time.ctime())

    time.sleep(4)
    print('end loopl at:', time.ctime())

def loopl2():
    print('start loopl2 at :', time.ctime())

    time.sleep(2)
    print('end loopl2 at:', time.ctime())

def main():
    print("starting at:", time.ctime())
    #loopl()
    #loopl2()
    _thread.start_new_thread(loopl, ())
    _thread.start_new_thread(loopl2, ())
    print("all done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
'''
#再遍历一次列表，给每一行加上缩进，一个缩进为四个空格
for m in range(len(str)):
    #如果某行有‘}’把之后的每一行减少一个缩进
    if '}' in str[m]:
        for z in range(m+1,len(str)):
            w = str[z].count(kg)
            str[z] = str[z].replace(kg,'')
            str[z] = kg*(w-1) +str[z]
    #将修改好的列表str写进java文本中
    f2.write(str[m])'''


'''
    if m < (len(str)-1) and '{' not in str[m] and '{' not in str[m+1]:
        x = str[m].count(kg)
        str[m+1] = kg*x + str[m+1]'''
#再遍历一次列表，给每一行加上缩进，一个缩进为四个空格
for m in range(len(str)):
    #如果某行有‘}’把之后的每一行减少一个缩进
    if '}' in str[m]:
        w = str[m].count(kg)
        for z in range(m,len(str)-1):
            str[z+1] = kg*(w-1) +str[z+1]