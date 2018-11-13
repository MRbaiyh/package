a = "A"
b = "B"
c = "C"
def hano(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
        return None
    if n == 2:
        print(a,"-->",b)
        print(a,"-->",c)
        print(b,"-->",c)
        return None
    hano(n-1,a,c,b)
    print(a,"-->",c)
    hano(n-1,b,a,c)
    
#n=4
#hano(n,a,b,c)
a = [1,2,3,4,5]
length = len(a)
index = 0
while index < length:
    print(a[index])
    index += 1

def af(n):
    n[2] = 300
    print(n)
    return None

def bf(n):
    n += 100
    print(n)
    return None

bn = 9
print(a)
print(id(a))
af(a)
print(a)
print(id(a))
print(bn)
bf(bn)
print(bn)

x = a[1::1]
print(x)

z = {}
w = {1,2,3}
ww = dict(a=1,s=2,d=3)
for k,v in ww.items():
    print(k,'---',v)
zz = (1,2,3)
zzz = []
print(type(z))
print(type(w))
print(type(ww))
print(type(zz))
print(type(zzz))

class Animel():
    def __init__(self):
        print("lalala")

class PXdw(Animel):
    def __init__(self, name):
        print("paxing dongwu {0}".format(name))

class dog(PXdw):
    pass

d = dog("kk")
sss = Animel()