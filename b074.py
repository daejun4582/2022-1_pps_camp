def calculate(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

def collect(n,memory):
    l = []
    while 1:
        if n in memory:
            return True, l
        else:
            l.append(n)
            if n ==1:
                return True,l
            n = calculate(n)