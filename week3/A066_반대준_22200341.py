n = input()
l = []
for i in range(len(n)):
    l.append(int(n[i]))
l.sort(reverse = True)
l = list(map(str,l))
result = "".join(l)
print(result)