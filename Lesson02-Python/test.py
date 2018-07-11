def f(x, y, z):
    print(x, y, z)
    
args=(1, 2, 3)
f(*args)

kwargs = {'y':1, 'x':2, 'z':3 }
f(**kwargs)