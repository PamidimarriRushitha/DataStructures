#lcm of array elements

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return (a*b)//gcd(a,b)
a=[int(x) for x in input().split()]
n=lcm(a[0],a[1])
for i in range(2,len(a)):
    n=lcm(n,a[i])
print(n)
