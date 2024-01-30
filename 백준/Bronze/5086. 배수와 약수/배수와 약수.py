import sys

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        if n > m and n % m == 0:
            sys.stdout.write(str('multiple')+"\n")
        elif m >= n and m % n == 0:
            sys.stdout.write(str('factor')+"\n")
        else:
            sys.stdout.write(str('neither')+"\n")