import sys

n, m = map(int, input().split())
a = [False]*n
b = [0]*m

li = list(map(int, input().split()))
li.sort()

# print(li)

def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, b)) + '\n')
        return
    
    for i in range( n):
#         if a[i] == True:
#             continue

        b[index] = li[i]
#         a[i] = True
        go(index+1, n, m)
#         a[i] = False

go(0, n, m)