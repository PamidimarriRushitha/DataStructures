#bubble sort
#print each iteration

def bubbleSort(n,arr):
    for i in range(1,n+1):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(*arr)
n=int(input())
a=[int(x) for x in input().split()]
bubbleSort(n,a)
