import sys

cnt = int(input())
divisors = list(map(int, input().split()))

divisor_max = max(divisors)
divisor_min = min(divisors)
num = divisor_max * divisor_min

sys.stdout.write(str(num))