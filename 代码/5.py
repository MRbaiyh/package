import os
print(os.name)
# linux 中点好. 代表当前目录， 双点..代表父目录
# abspath() 将路径转化为绝对路径
#''' 格式：os.path.abspath('路径') '''

l1 = [1,2,3]
print(l1)
def multen(n):
    return n * 10
l2 = map(multen, l1)
print(list(l2))