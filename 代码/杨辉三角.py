#输出杨辉三角方法1
def yanghui1(k):           #k代表想输出多少行杨辉三角
    l1 = [1]               #设置杨辉三角的第一行为1
    print(l1)
    for i in range(k):    #利用列表的连接去输出杨辉三角的每一行
        l1 = [1] + [l1[j+1]+l1[j] for j in range(len(l1)-1)] + [1]
        print(l1)
yanghui1(5)                #输出5行杨辉三角

#输出杨辉三角方法2
def yanghui2():              
    l2 = [[1],[],[],[],[],[]]             #设置一个二维列表，第一行值为1
    print(l2[0])                    #输出第一行
    for i in range(1,len(l2)):
        l2[i].append(1)                   #设置第i行的列表的第一个数为1
        for j in range(1, i):
            l2[i].append(l2[i-1][j]+l2[i-1][j-1])     #添加列表中间的数，为上一行本列的值加上上一行前一列的值
        l2[i].append(1)                   #设置第i行的列表的最后一个数为1
        print(l2[i])                      #输出第i行
yanghui2()