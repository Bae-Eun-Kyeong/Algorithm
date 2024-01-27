import sys

n = int(input())
total_sum = 0

for i in range(1, n+1):
    total_sum += i* (n//i)
sys.stdout.write(str(total_sum)+'\n')
