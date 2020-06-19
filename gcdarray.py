#gcd of array elements

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

a=[int(x) for x in input().split()]
n=gcd(a[0],a[1])
for i in range(2,len(a)):
    n=gcd(n,a[i])
print(n)
