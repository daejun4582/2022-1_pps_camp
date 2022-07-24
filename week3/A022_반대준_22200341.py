import sys
input = sys.stdin.readline
def m(n):
    total = 0
    total += (n//60)*15+15
    return total

    
    
def y(n):
    total = 0
    total += (n//30)*10+10
    return total




n = int(input())
calls = list(map(int,input().split()))
total_y = 0
total_m = 0

for call in calls:
    total_m += m(call)
    total_y += y(call)

if(total_m>total_y):
    print(f'Y {total_y}')
elif(total_m==total_y):
    print(f'Y M {total_y}')
else:
    print(f'M {total_m}')