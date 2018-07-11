def f(x,y):
    tmp=x
    x=y
    y=tmp
    return (x,y)

a=2
b=3
r=f(a,b)
print(r)