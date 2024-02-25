import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
li = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int, input().split())
    li[u].append(v)
    li[v].append(u)

cnt = 0
tf_bfs = [False]*(n+1)

def bfs(x):
    que = deque([])
    que.append(x)
    tf_bfs[x] = True

    while que:
        n = que.popleft()
        for i in li[n]:
            if tf_bfs[i] == False:
                que.append(i)
                tf_bfs[i] = True

for j in range(1, n+1):
    if tf_bfs[j] == False:
        cnt += 1
        bfs(j)

sys.stdout.write(str(cnt))