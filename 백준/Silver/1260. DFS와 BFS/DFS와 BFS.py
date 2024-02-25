n, m, v = map(int, input().split())
li = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

for q in li:
    q.sort()

# print(li)

tf = [False]*(n+1)
pr = []

def dfs(x):
    tf[x] = True
    pr.append(x)

    for i in li[x]:
        if tf[i] == True:
            continue
        elif tf[i] == False:
            dfs(i)

dfs(v)
print(*pr)

tf_bfs = [False]*(n+1)
pr_bfs = []
def bfs(x):
    que = []
    que.append(x)
    tf_bfs[x] = True
    pr_bfs.append(x)

    while que:
        n = que.pop(0)
        for i in li[n]:
            if tf_bfs[i] == False:
                que.append(i)
                tf_bfs[i] = True
                pr_bfs.append(i)

bfs(v)
print(*pr_bfs)