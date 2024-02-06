import sys

n, m = map(int, input().split())
# a: 각 숫자가 수열에 이미 사용되었는지 알아보는 배열
a = [False]*n
b = [0]*m


def go(index, n, m):
    # index: 현재 수열의 위치
    
    if index == m:
        # index와 m이 같아지면 b배열에 m개의 숫자가 들어가 있음을 의미
        sys.stdout.write(' '.join(map(str,b)) + '\n')
        return

    for i in range(n):
        # 인덱스는 0부터이므로 i+1로 저장 =>  자연수 1부터 시작하는 것으로 맞추기
        b[index] = i+1
        a[i] = True
        go(index+1, n, m)
        a[i] = False

go(0, n, m)