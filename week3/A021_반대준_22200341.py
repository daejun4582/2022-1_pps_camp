import sys

input = sys.stdin.readline
n = int(input())
total = 0
for i in range(n):
    plug = int(input())
    if i==n-1:
        total +=plug
    else:
        total +=plug-1
print(total)