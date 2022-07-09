data = dict(zip([i for i in range(0,10)],[0]*10))
a = input()

for i in a:
    data[int(i)]+=1

if data[6]!= data[9]:
    w = 6 if data[6]>data[9] else 9 
    d = ((max(data[6],data[9]) - min(data[6],data[9]))+1) //2 +data[6 if w!=6 else 9]
    data[w] = d

b = max(data,key = data.get)

print(data[b])