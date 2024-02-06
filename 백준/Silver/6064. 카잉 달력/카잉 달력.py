t = int(input())
ans = 1

for _ in range(t):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x

    while k < n*m:
        if k % n == y:
            print(k+1)
            break
        k += m
        # x가 k일 때 값을 반복해서 돌게 됨
    else:
        print(-1)