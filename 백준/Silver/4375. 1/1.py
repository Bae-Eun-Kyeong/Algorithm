while True:
    try:
        n = int(input())
    except:
        break

    x = 0
    i = 1

    while True:
        x = x*10 +1
        x %= n
        if x == 0:
            print(i)
            break
        i += 1
