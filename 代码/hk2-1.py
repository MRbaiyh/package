import math
def equation(a,b,c):
    m = b*b - 4*a*c
    if m == 0 :
        x1 = x2 = -b/(2*a)
        return x1
    elif m > 0 :
        x1 = (-b + math.sqrt(m))/(2*a)
        x2 = (-b - math.sqrt(m))/(2*a)
        return x1,x2
    else:
        print('此方程无解！！')

a = float(input('输入a的值：'))
b = float(input('输入b的值：'))
c = float(input('输入c的值：'))
print(equation(a,b,c))


