def checkUni(lst):
    return len(set(lst)) == 8

def check_x(lst):
    X=[]
    for i in lst:
        X.append(i[0])
    print(X)
    return checkUni(X)

def check_y(lst):
    Y=[]
    for i in lst:
        Y.append(i[1])
    print(Y)
    return checkUni(Y)

def check_pos(lst):
    Pos=[]
    for i in lst:
        Pos.append(i[0]+i[1])
    print(Pos)
    return checkUni(Pos)

def check_neg(lst):
    Neg=[]
    for i in lst:
        Neg.append(i[0]-i[1])
    print(Neg)
    return checkUni(Neg)

def eight_queens(arq):
    checkList=[check_x,check_y,check_pos,check_neg]
    result=[f(arq) for f in checkList]
    print(result)
    if False in result:
        return False
    else:
        return True
    

r=eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])
print(r)