#next greatest number with these digits

from itertools import permutations
s=str(input())
l=list(s)
m=list(permutations(l,len(s)))
r=[]
for i in range(len(m)):
    t=list(m[i])
    t="".join(t)
    if t>s:
        r.append(t)
if len(r)>0:
    print(min(r))
else:
    print(-1)
