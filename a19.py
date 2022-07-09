a = int(input())
b = int(input())
c = int(input())
answer = a*b*c
s = str(answer)
data = dict(zip([i for i in range(0,10)],[0]*10))

for i in range(len(s)):
    data[int(s[i])]+=1

for x in data.values():
    print(x)