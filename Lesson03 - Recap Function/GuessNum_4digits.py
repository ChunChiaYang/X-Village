import random
def set_answer():
    ans=format(random.randint(0,1000),"04")
    return ans

def judge_guess(ans,num):
    if ans==num:
        print("Right!!!")
        return 0
    else:
        A,B=0,0
        copy_ans=ans.copy()
        for i in range(4):
            if num[i]==copy_ans[i]:
                copy_ans[i]='*'
                num[i]='#'
                A=A+1
        for i in range(4):
            if num[i] in copy_ans:
                copy_ans[copy_ans.index(num[i])]='*'
                num[i]='#'
                B=B+1
        print(A,'A',B,'B')
        return 1

flag=1
while flag:
    ans=list(set_answer())
    print(ans)
    flag1=1
    while flag1:
        num=list(input("Plz enter a number with 4 digits:"))
        print(ans)
        flag1=judge_guess(ans,num)
    flag=int(input("Do you want to play again? Yes:1,No:0 :"))









