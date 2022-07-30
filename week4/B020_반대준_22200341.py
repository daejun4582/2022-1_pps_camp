import sys
sys.setrecursionlimit(10 ** 6)


# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y, number):
    number += graph[x][y]


    if len(number) == 6:
        if number not in result:
            result.append(number)
        return


    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]


        if 0 <= a < 5 and 0 <= b < 5:
            dfs(a, b, number)



graph = [list(map(str, sys.stdin.readline().split())) for i in range(5)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(result))