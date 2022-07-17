def l(a):
    i = 1
    while 1:
        a = a-i
        if a<=0:
            return a+i,i
        i+=1
    return a,i

def s(a,i):
    sum = 0
    for j in range(i):
        sum+=j**2
    sum += (a+1)*(i)
    print(sum)
    return sum

a,b = map(int,input().split())
x,y= l(a)
c,d = l(b)
print(s(c,d)-s(x,y))