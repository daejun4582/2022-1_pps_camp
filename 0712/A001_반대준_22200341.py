def findContentChildren( g, s):    
    i = 0
    count = 0
    g.sort()
    s.sort()
    
    for  j in range(len(s)):
        if i<len(g) and g[i]<=s[j]:
            i+=1
    return i

g = [1]
s = [1,2,3]
print(findContentChildren(g,s))