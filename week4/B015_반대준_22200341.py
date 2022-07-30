import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6) 
n=int(input()) 
b=list(map(int, input().split())) 
s=int(input()) 
cnt=1 
v=[0]*n 
def dfs(x):
    global cnt
    for nx in (x+b[x], x-b[x]):
        if 0<=nx<n and v[nx]==0:
            cnt+=1;v[nx]=1
            dfs(nx)
dfs(s-1)
print(cnt)