def fib(self, n: int) -> int:
    t = [0,1]
    for i in range(2,n+1):
        t.append(t[i-1]+t[i-2])
    return t[n]