import sys

n, m = map(int, input().split())

def factor(a):
    li=[]
    for i in range(1, a+1):
        if a % i == 0:
            li.append(i)
    return li

li_n = factor(n)
li_m = factor(m)

common_li = set(li_n)&set(li_m)

factor_max = max(common_li)
multiple_min = factor_max * (n // factor_max) * (m // factor_max)

sys.stdout.write(str(factor_max) + "\n")
sys.stdout.write(str(multiple_min) + "\n")