import sys
from collections import deque

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():

    while q:
        # x : a물통의 물의 양, y : b물통의 물의 양, z : c물통의 물의 양
        x, y = q.popleft()
        z = c - x - y

        # a 물통이 비어있는 경우 c 물통에 남아있는 양 저장
        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, c-z)
        pour(x - water, y)
        # y -> x
        water = min(y, a-x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, c-z)
        pour(x, y - water)
        # z -> x
        water = min(z, a-x)
        pour(x + water, y)
        # z -> y
        water = min(z, b-y)
        pour(x, y + water)



a, b, c = map(int, sys.stdin.readline().split())


q = deque()
q.append((0, 0))


visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True


answer = []

bfs()


answer.sort()
for i in answer:
    print(i, end=" ")