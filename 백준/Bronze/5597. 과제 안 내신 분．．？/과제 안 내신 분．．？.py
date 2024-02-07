import sys

li = []

for _ in range(28):
    n = int(input())
    li.append(n)
    

for i in range(1, 31):
    if i not in li:
        sys.stdout.write(str(i)+" ")