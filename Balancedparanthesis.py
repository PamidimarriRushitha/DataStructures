
#Balanced Paranthesis

def isBalanced(n):
    stk=[]
    open_=['[','{','(']
    close=[']','}',')']
    for i in n:
        if i in open_:
            stk.append(i)
        elif i in close:
            pos=close.index(i)
            if len(stk)>0 and open_[pos]==stk[len(stk)-1]:
                stk.pop()
            else:
                return False
    if len(stk)==0:
        return True
    else:
        return False
n=input()
if isBalanced(n):
    print('yes')
else:
    print('no')
