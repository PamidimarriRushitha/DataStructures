def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
n=int(input())
s=input().split()
lcm=int(s[0])
for i in s[1:]:
    lcm=lcm*int(i)/gcd(lcm,int(i))
print(int(lcm))
