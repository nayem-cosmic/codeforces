import sys

input = sys.stdin.readline
output = []

t = int(input())

for i in range(t):
    input()
    lst = list(map(int, input().split()))
    dir = [True]*len(lst)
    
    asc = False
    while not asc:
        asc = True
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                dir[j], dir[j+1] = not dir[j+1], not dir[j]
                asc = False
    
    if all(dir):
        output.append('YES')
    else:
        output.append('NO')
        
for l in output:
    print(l, flush=True)
