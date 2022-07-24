def addDigits(self, num: int) -> int:
    
    temp = str(num)
    while True:
        x = 0
        if(len(temp)==1):
            break
        else:
            for i in range(len(temp)):
                x+=int(temp[i])
            temp = str(x)
    return temp
        