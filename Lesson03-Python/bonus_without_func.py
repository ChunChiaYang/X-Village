A={"grade":91,"hour":20}
B={"grade":75,"hour":15}
C={"grade":60,"hour":25}
D={"grade":75,"hour":10}
E={"grade":80,"hour":12}
F={"grade":90,"hour":25}
G={"grade":45,"hour":14}
H={"grade":95,"hour":13}
I={"grade":88,"hour":2}

staff={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I}

for i in staff:
    salary=0
    if staff[i]['grade']>90:
        salary=salary+8000
    elif staff[i]['grade']>=70 and staff[i]['grade']<=90:
        salary=salary+6000
    elif staff[i]['grade']<70:
        salary=salary+4000
    salary=salary+staff[i]['hour']*200
    print(i,":",salary)


    

