import sys
input = sys.stdin.readline

n = int(input())
datas =[]
for i in range(n):
    num,name = input().split()
    datas.append([int(num),name])
    
datas.sort(key = lambda x: x[0])

for data in datas:
    print(f'{data[0]} {data[1]}')