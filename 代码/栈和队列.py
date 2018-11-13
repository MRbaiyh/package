#利用列表实现进出栈
print("----进出栈操作----")
list1 = []
#进栈
for i in range(5):
    print("请为栈输入元素：", end = "")
    list1.append(input())
print(list1)
#出栈
for i in range(len(list1)):
    list1.pop()
    print(list1)

#利用列表实现进出队列
print("----进出队列操作-----")
list2 = []
#进队列
for i in range(5):
    print("请为队列输入元素：", end = "")
    list2.append(input())
print(list2)
#出队列
for i in range(len(list2)):
    list2.pop(0)
    print(list2)