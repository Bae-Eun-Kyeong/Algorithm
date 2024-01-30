import sys

n, k = map(int, input().split())
li = []

for i in range(1, n+1):
    if n % i == 0:
        li.append(i)
        
if len(li) < k:
    sys.stdout.write(str(0))
else:
    sys.stdout.write(str(li[k-1]))