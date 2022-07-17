import sys

a,b = map(int,input().split())
data = list(map(int,sys.stdin.readline().split()))
prefix_sum = [sum(data[0:0+b])]

for i in range(a-b):
        prefix_sum.append(prefix_sum[i]-data[i]+data[i+b])
        
print(max(prefix_sum))