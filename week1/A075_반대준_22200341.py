def solution(numbers):
    answer = ''
    d = list(map(str,numbers))
    d = sorted(d, key = lambda x:x*10, reverse=True)
    for i in d:
        answer +=i 
    if int(answer) == 0:
        return '0'
    return answer
        
print(solution([3, 30, 34, 5, 9]))