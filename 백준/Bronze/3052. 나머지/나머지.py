import sys

li = []

for _ in range(10):
    n = int(input())
    remainder = n % 42
    
    if remainder not in li:
        li.append(remainder)
        
sys.stdout.write(str(len(li)))