import sys

def check(a):
    # n은 행의 개수
    n = len(a)
    
    # 최종적으로 가장 긴 연속 배열 길이
    ans = 1
    
    for i in range(n):
        cnt = 1
        
        # 수평 탐색
        for j in range(1, n):
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt=1
        
        # 수직 탐색
        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


n = int(input())
a = [list(input()) for _ in range(n)]
ans = 0
        
# 인접한 원소와 위치를 바꾸어가며 연속배열 확인 
for i in range(n):
    for j in range(n):
        #  수평 교환
        if j+1 < n:
            a[i][j], a[i][j+1] =  a[i][j+1], a[i][j]
            temp = check(a)
            if ans < temp:
                ans =  temp
            a[i][j], a[i][j+1] =  a[i][j+1], a[i][j]
        
        # 수직 교환
        if i+1 < n:
            a[i][j], a[i+1][j] =  a[i+1][j], a[i][j]
            temp = check(a)
            if ans < temp:
                ans =  temp
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
        
sys.stdout.write(str(ans))