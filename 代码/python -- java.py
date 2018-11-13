import os
# 打开写有python代码的文件，并将它的每一行读出来存放在列表str里面
f = open('python.txt', 'rt')
str = f.readlines()
#print(str)
#以只写的方式新建一个java文件，用于存放java格式代码
f2 = open('java.txt','wt')
kg = '    '
#首先先写入固定格式的java代码开头
content = 'public class ' + input('请输入类名：') + '{' + '\n' + '    public static void main(String args[]){' + '\n'
f2.write(content)
#遍历列表的每一行
for i in range(len(str)):
    #把每一行的空格全部去掉
    str[i] = str[i].replace(kg, '')
    #遇见python中的‘：’把其替换为‘{’
    if ':' in str[i]:
        str[i] = str[i].replace(':','{')
    #遇见pytho中的‘for’将其改为java格式的for循环
    if 'for' in str[i]:
        cs = str[i][4]
        a = str[i][16]
        b = str[i][19]+str[i][20]
        str[i] = 'for(int '+ cs + ' = ' + a + '; '+cs+' < ' + b + '; ' + cs + '++){' + '\n'
    #遇见python中第一个赋初值的代码，将其改为java格式在前面加上数据类型
    if ' = True' in str[i]:
        str[i] = 'boolean ' + str[i]
    #在没有‘{‘的在代码末尾加上';'
    if '{' not in str[i]:
        str[i] = str[i].replace('\n','')
        str[i] = str[i] + ';' + '\n'
    #如果python代码中有if判断语句，将其改为java格式
    if '==' and 'if' in str[i]:
        list1 = list(str[i])
        list1[2] = '('
        wz = str[i].find('{')
        list1[wz] = '){'
        str[i] = ''
        for j in range(len(list1)):
            str[i] = str[i] + list1[j]
    if 'flag' in str[i]:
        str[i] = str[i].replace('True','true')
        str[i] = str[i].replace('False','false')
    #把python的print改成java的print格式
    if 'print' in str[i]:
        str[i] = str[i].replace('print','System.out.println')
        str[i] = str[i].replace(', end = \'\' )','')
        str[i] = str[i].replace('( "%d   "%( i )','(i)')

#再遍历一次列表，给每一行加上缩进，一个缩进为四个空格
for m in range(len(str)): 
    #给列表第一行前加上2个缩进
    if m == 0:
        str[0] = kg*2 + str[0]
    #如果某行存在'{'在其下一行加上一个缩进
    if '{' in str[m] and m < (len(str)-1):  
        x =  str[m].count(kg)  
        str[m+1] = kg*(x+1) + str[m+1]
    #如果本行没有'{',在下一行加本行有的缩进个数
    if m < (len(str)-1) and '{' not in str[m]:
        x =  str[m].count(kg)
        str[m+1] = kg*x +str[m+1]
    #如果存在'if'进行如下处理
    if 'if' in str[m]:
        flag = True
        #在这个if语段中存在‘break’在'break'后加上'}'
        for k in range(m,len(str)):
            if 'break' in str[k]:
                str[k] = str[k].replace('\n','')
                #末尾加上两个括号结束循环
                str[k] = str[k] + '}}' + '\n'
                flag = False
        #如果没有'break'则在下一行加上‘}’
        if flag == True:
            str[m+1] = str[m+1].replace('\n','')
            str[m+1] = str[m+1] + '}' + '\n'
    #将修改好的列表str写进java文本中
    f2.write(str[m])

#加‘}’操作
for y in range(3):
    f2.write('}\n')
 
#关掉两个文件
f.close()
f2.close()