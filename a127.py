#beakjun 1934
def GCD(a,b):
    temp = a%b
    if temp ==0:
        return b    
    return GCD(b,temp)

def LCM(a,b,c):
    return (a*b)//c


n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    print(LCM(a,b,GCD(a,b)))