import math as m
'''
комбинированный метод

'''
def func(x):
    return x**2-2+2*m.sin(x)
def first(x):
    return 2*x+2*m.cos(x)
def second(x):
    return 2-m.sin(x)

a=int(input("a=")) #a=-2
b=int(input("b=")) #b=-1
e=0.001
k=0

while func(a)*func(b)>=0:
    print("Введен неправильный интервал")
    a=int(input("a="))
    b=int(input("b="))

p=0.5*m.fabs(b-a)

if not func(b)*second(b)>0:
    c=a
    a=b
    b=c
while (p>e):
    a=b-(func(b)*(b-a))/(func(b)-func(a))
    b=b-func(b)/first(b)
    k+=1
    p=0.5*m.fabs(b-a)

ans=(a+b)/2
print(ans,"+-",p)
print(k)



