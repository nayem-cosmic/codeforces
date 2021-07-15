import sys

def check_all_zero(l):
    for e in l:
        if e != 0:
            return False
    
    return True

input = sys.stdin.readline
output = []

t = int(input())

for i in range(t):
    input()
    a = map(int, input().split())
    b = map(int, input().split())
    
    d = [h-k for h, k in zip(a, b)]
    if sum(d) != 0:
        output.append(-1)
    elif check_all_zero(d):
        output.append(0)
    else:
        neg = []
        pos = []
        while check_all_zero(d) == False:
            for j in range(len(d)):
                if d[j] < 0:
                    d[j] += 1
                    pos.append(j+1)
                elif d[j] > 0:
                    d[j] -= 1
                    neg.append(j+1)
        
        output.append(len(neg))
        for h, k in zip(neg, pos):
            output.append(f"{h} {k}")

for l in output:
    print(l)
