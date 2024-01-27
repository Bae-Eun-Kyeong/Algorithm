def mod_length(n):
    x = 1
    l = 1
    while True:
        if x % n == 0:
            return l
        
        x = (x * 10 + 1) % n
        l += 1

while True:
    try:
        n = int(input())
        print(mod_length(n))
    except:
        break