def s(st):
    count=0
    for i in st:
        if i.isalpha()==False:
            count+=int(i)
           
    return count
     
n = int(input())
data = []

for i in range(n):
    data.append(input())

data.sort()
data.sort(key = lambda x: s(x))
data.sort(key = lambda x: len(x))

for result in data:
    print(result)