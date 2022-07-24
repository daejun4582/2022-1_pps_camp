#sieve of Eratosthenes
def countPrimes(n):
    l = [False,False]+[True]*(n-1)
    primes = []
    
    for i in range(2,n):
        if l[i]:
            primes.append(i)
            for j in range(2*i,n+1,i):
                l[j]=False
    return len(primes)

print(countPrimes(100000))