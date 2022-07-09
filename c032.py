n = int(input())
nums_up = 1     #벌집 개수 1개 부터 시작
level = 1

while n>nums_up:
    nums_up += 6*level
    level +=1
print(level)