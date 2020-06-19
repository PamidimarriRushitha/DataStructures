#right rotated array after k operations

n=int(input())
s=input()
a=[]
b=[]
rem=n%len(s)
for i in range(0,len(s)-rem):
    a.append(s[i])
for i in range(len(s)-rem,len(s)):
    b.append(s[i])
print(b+a)
