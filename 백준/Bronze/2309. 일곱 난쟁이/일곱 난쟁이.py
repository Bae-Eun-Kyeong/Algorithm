import sys

tall = []

for i in range(0, 9):
    i = int(input())
    tall.append(i)
    
tall_sum = sum(tall)

for a in range(0, 9):
    for b in range(a+1, 9):
        test = tall_sum - tall[a] - tall[b]
        if test == 100:
            result = [tall[i] for i in range(9) if i != a and i!=b]
            result.sort()
            for item in result:
                sys.stdout.write(str(item)+"\n")
            sys.exit(0)