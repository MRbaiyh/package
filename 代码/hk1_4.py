list = [1,2,3,4,5,6,7,8]
for i in range(len(list)):
    print(list[i], end = " ")
print()
for i,k in enumerate(list):
    print("第{0}元素是：{1}".format(i,k))

t = (1,2,3,'ss','sad')
for i in range(len(t)):
    print(t[i], end = " ")
print()
for i,k in enumerate(t):
    print("第{0}元素是：{1}".format(i,k))

dic = {'Name':'mark','Age':'18','Habit':'ball','Sex':'Man'}
for key in dic.keys():
    print(key,dic[key])
for value in dic.values():
    print(value)

s = {1,3,435,'sad',23,'asda','萨达'}

for i in s:
    print(i, end = " ")