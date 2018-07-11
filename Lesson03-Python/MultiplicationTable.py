def f(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,'*',j,'=',i*j,sep='',end='\t')
        print('')

m=9
f(m)