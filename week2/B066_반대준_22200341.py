def reverseString(s):
    
    for i in range(len(s)//2):
        last=-(i+1)
        s[i],s[last]=s[last],s[i]
    
    return s