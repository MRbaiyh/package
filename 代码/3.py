class student():
    def __init__(self, name):
        self.name = name

    def __gt__(self, oo):
        print("哈哈，{0} 会比 {1} 大吗？".format(self.name, oo.name))
        return self.name > oo.name
stu1 = student("one")
stu2 = student("two")

print(stu1 > stu2)

class ad():
    name = "haha"

    def fget(self):
        print("aiwo")
        return "-" * 10
    def fset(self, name):
        print("我爱重庆")
        self.name = "重庆" + name
        print(self.name)
    def fdel(self):
        pass
    ww = property(fget,fset,fdel,"这是我自己")
a = ad()
print(a.name)
print(a.ww)

class A():
    pass
def say(self):
    print("Saying... ...")

A.say = say
a = A()
a.say()
#同样也可以记住methodtype
#用type来创建一个类

def talk(self):
    print("saying... ...")
def listen(self):
    print("I am hearing... ...")

A = type("me", (object,),{"talk": talk,"hear": listen})

A.talk

#元类演示
#元类写法是固定的，必须继承自type
#元类一般命名MetaClass结尾
class byhMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print("元类")
        attrs['id'] = '00000'
        attrs['addr'] = "重庆市大渡口区"
        return type.__new__(cls, name, bases, attrs)

class Teacher(object, metaclass=byhMetaClass):
    pass

t = Teacher()
