data = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
l = []
for i in word:
    l.append(i)

cor = 0
for letter in data:
    cc = []
    for i in range(0,len(word)):
        if i+len(letter)<=len(word):
            if letter in word[i:i+len(letter)] and "_" not in l[i:i+len(letter)]:
                for j in range(i,i+len(letter)):
                    l[j] = '_'
                cor+=1

for i in l:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        cor +=1

    
print(cor)