import math

def combin(r,n):
    return int (math.factorial(r)/math.factorial(r-n)/math.factorial(n))

h=12

for i in range(h):
    print(" "*(h-i-1),end='')
    for j in range(i+1):
        print(combin(i,j),end=' ')
    print('')




