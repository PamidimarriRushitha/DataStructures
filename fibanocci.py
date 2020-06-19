#print 'n' terms of fibonacci series

n=int(input())
n1=0
n2=1
l=[]
l.append(n1)
l.append(n2)
for i in range(2,n):
    n3=n1+n2
    l.append(n3)
    n1=n2
    n2=n3
print(*l)
