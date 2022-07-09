n = int(input())
l = [[0,0]]*n

for i in range(n):
    l[i] = list(map(int,input().split()))

l.sort(key = lambda x: (x[0],x[1]))

for  i in range(n):
    print(l[i][0],l[i][1])
     