def hihi(data):
    a = True
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]== data[j] and j-1 !=i :
                for k in range(i,j):
                    if data[i] != data[k]:
                        a = False
                        break
                    else:
                        a =  True
        if a == False:
            break
    return a

n = int(input())
sum = 0

for i in range(n):
    a = hihi(input())
    if a == True:
        sum+=1

print(sum)