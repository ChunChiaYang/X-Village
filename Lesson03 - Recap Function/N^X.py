def maker(n):
    return lambda x:n**x

f=maker(9)
print(f(5))