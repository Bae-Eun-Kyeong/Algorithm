import sys

n = int(input())
m = list(map(int, input().split()))
cnt = 0

def factor(a):
    li = []
    for i in range(1, a+1):
        if a % i ==0:
            li.append(i)
    return li

for i in range(0, n):
    factor_li = factor(m[i])

    if len(factor_li) == 2:
        cnt += 1

sys.stdout.write(str(cnt))