n= int(input())
sum = 0
k = 0
l = []
h = []
for i in range(n):
    k = int(input())
    l.append(k)
    if k == 0:
        del h[-1]
    else:
        h.append(i)



for x in h:
    sum+=l[x]

print(sum)