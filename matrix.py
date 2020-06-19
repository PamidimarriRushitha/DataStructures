#sum of product of diagonals


n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
x=1
y=1
for i in range(n):
    for j in range(n):
        if i==j:
            x*=a[i][j]
        if i+j==n-1:
            y*=a[i][j]
print(x+y)
