a = list(map(int,input().split()))
if a[2]>a[1]:print(a[0]//(a[2]-a[1])+1)
else:print(-1)