def f(n):
    print(n)
    if n==1:
        return 1
    return f(n-1)*n

print(f(6))