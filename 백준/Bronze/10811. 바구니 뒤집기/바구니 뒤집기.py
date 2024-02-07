import sys

n, m = map(int, input().split())
li = []

for i in range(n):
    li.append(i+1)
# print(li)

for j in range(m):
    x, y = map(int, input().split())
    li[x-1: y]= li[x-1:y][::-1]
    
for num in li:
    sys.stdout.write(str(num)+" ")