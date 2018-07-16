A={"grade":55,"hour":14}
B={"grade":96,"hour":13}
C={"grade":85,"hour":22}

def CountSalary(grade,hour):
    salary=0
    if grade>90:
        salary=salary+8000
    elif grade<=90 and grade>=70:
        salary=salary+6000
    elif grade<70:
        salary=salary+4000
    salary=salary+hour*200
    return salary

staff={'A':A,'B':B,'C':C}
for i in staff:
    print(i,':',CountSalary(staff[i]["grade"],staff[i]["hour"]))