# 시간 초과 뜸
# def calculate(n):
#     if n%2==0:
#         return n//2
#     else:
#         return 3*n+1

# def collect(n,memory):
    
#     count= 0
#     if n ==1:
#         return 0
#     else:
#         while 1:
#             if n in memory.keys():
#                 count+= memory[n]
#                 print("use")
#                 break
#             else:
#                 count+=1
#                 if n ==1:
#                     break
#             n = calculate(n)
#         return count 

# def conject(n):
#     memory = {}
#     for i in range(1,n+1):
#         memory[i] = collect(i,memory)
        
    
#     return -1 if memory[n]>500 else memory[n]

# print(conject(626331))

def solution(num):
    if num == 1:
        return 0    
    else:
        count = 0
        i = 0
        while 1:
            if count<500:
                if num == 1:
                    i = count
                    break
                else:
                    if num%2==0:
                        num //= 2
                        count+=1
                    else:
                        num = num*3+1
                        count+=1
            else:
                i = -1
                break  

        return i
print(solution(626331))