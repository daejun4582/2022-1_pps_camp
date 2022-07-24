n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse = True)

s = sum(list(map(lambda x: a[x]*b[x],range(0,n))))
print(s)