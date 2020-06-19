#Medium Aliens Problem

n=input()
c=[int(x) for x in input().split()]
beta=0
gamma=0
def maxIndex(c):
    u=0
    for k in range(len(c)):
        if c[u]<c[k]:
            u=k
    return u
flag=False
while True:
    beta+=c[maxIndex(c)]
    c[maxIndex(c)]//=3
    if beta>=1000:
        flag=True
        print("Beta")
        break
    gamma+=c[maxIndex(c)]
    c[maxIndex(c)]//=3
    gamma+=c[maxIndex(c)]
    c[maxIndex(c)]//=3
    if gamma>=1000:
        flag=True
        print("Gamma")
        break
    if max(c)==0:
        break
if not flag:
    print(-1)
