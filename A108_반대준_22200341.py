#수 뒤집기 baekjun 3062
def reverse_sum(a):
    return int(a)+int("".join(list(reversed(a))))
    
def pelindrom(a):
    return int("".join(list(reversed(str(a))))) == a    
    
for i in range(int(input())): 
    print("YES" if pelindrom(reverse_sum(input()))==1 else  'NO')