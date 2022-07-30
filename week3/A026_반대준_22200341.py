def solution(x):
    answer = False
    temp = str(x)
    sum = 0
    for i in range(len(temp)):
        sum+= int(temp[i])
    if x%sum==0:
        answer = True
    return answer