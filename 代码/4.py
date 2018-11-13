import sys

print(type(sys.path))
print(sys.path)

class Parent():
    x = 4
    y = 5
    def sum(self, a, b):
        self.z = a + b
        print("求和结果为：{0}".format(self.z))
class son(Parent):
    def f(self):
        print(self.x+self.y)

a = input()
b = input()
t = son()
t.sum(int(a),int(b))
t.f()