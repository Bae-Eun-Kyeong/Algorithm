import sys

n = int(input())
m = int(input())

broken = [False] *10
if m > 0:
    a = list(map(int, input().split()))
else:
    a =[]

for i in a:
    broken[i] = True
    
def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c>0:
        if broken[c % 10]:
            # 고장난 숫자(True)라면 여기서 종료 -> 다음 수로 넘어가게 됨
            return 0
        l += 1
        c //= 10
    return l

# 이동채널 n - 현재 채널 100 : +/-버튼 사용한 최소 버튼 푸시 횟수(초기값 설정)
ans = abs(n-100)

# c: 현재 선택한 채널, n: 목표 채널
for i in range(0, 1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        # press: 숫자 외에 추가로 입력해야하는 +/- 횟수
        press = abs(c-n)
        if ans > l + press:
            ans = l + press
sys.stdout.write(str(ans))