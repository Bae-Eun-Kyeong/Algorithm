import sys

t = int(input())

def sum123(current_sum, n):
    ans = 0

    if current_sum == n:
        return 1
    if current_sum > n:
        return 0
        
    for i in range(1, 4):
        ans += sum123(current_sum + i, n)
        
    return ans


for _ in range(t):
    n = int(input())
    cnt = sum123(0, n)
    sys.stdout.write(str(cnt)+"\n")