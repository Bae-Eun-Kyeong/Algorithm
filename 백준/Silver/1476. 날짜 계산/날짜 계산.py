import sys

e, s, m = map(int, input().split())
year = 0

# 15 28 19 입력시 e, s, m이 0이 되므로 값이 나오지 않을 경우?
e -= 1
s -= 1
m -= 1

while True:
    if year % 15 == e and year % 28 == s and year % 19 == m:
        sys.stdout.write(str(year+1))
        break
    year += 1