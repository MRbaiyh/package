import random                                                                            #调用random，在随机输入年龄时使用
def student():
    a = 20170001                                                                         #初始学号为20170001
    FN = ['陈','赵','周','李','张']
    Sex = ['男','女']
    Age = [19,20]
    MN = ['德','昌','可','花','丽','霞']
    LN = ['坚','强','平']
    d = {'学号':'','姓名':'','年龄': '','性别':''}         #用于储存信息的字典
    for i in range(len(FN)):                                                            #利用循环输出所有姓名学生的信息
        d['年龄'] = random.choice(Age)                                                  #调用random.choice随机输入年龄
        for j in range(len(MN)):                                                       #判断性别
            if j<= 2 :
                d['性别'] = Sex[0]  
            else:
                d['性别'] = Sex[1]
                
            for k in range(len(LN)):
                d['学号'] = a 
                d['姓名'] = FN[i]+MN[j]+LN[k]
                a = a + 1                                                              #学号加一，进入下一个学生
                print(d) 
student()