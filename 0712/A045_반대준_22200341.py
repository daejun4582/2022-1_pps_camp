dic =dict(zip([chr(i) for i in range(97,123)],[0]*26))
a = input().lower()
max = -1
d = '_'
for letter in a:
    dic[letter]+=1
for k,v in dic.items():
    if max<v:
        max = v
        d = k
    elif max == v:
        d = '?'
print(d.upper())