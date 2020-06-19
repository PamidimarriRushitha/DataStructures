#addition of matrixes

n=int(input())
s=[]
l=[]
for i in range(n):
    p=[int(x) for x in input().split()]
    s.append(p)
print(s)
for i in range(n):
    o=[int(x) for x in input().split()]
    l.append(o)
print(l)
res=[[s[i][j]+l[i][j] for j in range(n)] for i in range(n)]
for i in res:
    print(*i)

