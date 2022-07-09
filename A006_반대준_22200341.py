s= input()
p = 0
y = 0
s = s.lower()
for i in s:
    if i== "p":
        p+=1
    if i =='y':
        y+=1
print(p==y)