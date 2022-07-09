import sys
n = int(input())
l = list(map(int,sys.stdin.readline().split()))
l.sort()
x = int(input())
count = 0
left = 0
right = n-1

while left<right:
    temp = l[left]+l[right]
    if temp == x:
        count+=1
        left+=1
    elif temp<x:
        left+=1
    else:
        right-=1

print(count)