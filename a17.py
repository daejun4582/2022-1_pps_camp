def co(a):
    data = dict(zip([i for i in range(0,10)],[0]*10))
    for i in range(len(a)):
        for j in range(0,10):
            if int(a[i]) == j:
                data[j]+=1
    return data
def m(data):
    max = -1
    w = 0
    for x,y in data.items():
        if max<y:
            max = y
            w = x
    if w in [0,1,2,3,4,5,7,8]:
        return max
    else:
        if (max- min(data[6],data[9])) %2 ==0:
            max = (max- min(data[6],data[9])) //2+min(data[6],data[9])
        else:
            max = (max- min(data[6],data[9]))+1 //2  +min(data[6],data[9])
    return max
a = input()
print(m(co(a)))


