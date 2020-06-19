#smallest number using digits of the number without changing size

n=input()
res=''
for i in range(1,10):
    res+=str(i)*n.count(str(i))
res=res[0]+(str(0)*n.count(str(0)))+res[1:]
print(res)
