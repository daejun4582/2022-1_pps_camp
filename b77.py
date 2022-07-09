def fibo(n,memo = {}):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            result = fibo(n-1,memo)+fibo(n-2,memo)
            memo[n] =  result
            # print(list(memo.values()))
            return result

print(fibo(int(input())))