def double_side_list(center,edge,gap):
    if center<edge:
        pass
    else:
        gap=-gap
    lst=[]
    lst.extend([i for i in range(center,edge,gap)])
    rev=lst[1:]
    rev.reverse()
    rev.extend(lst)
    lst=rev
    print(lst)
    
double_side_list(10,20,2)
