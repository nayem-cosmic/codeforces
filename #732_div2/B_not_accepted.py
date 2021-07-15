import sys

def word_val(w):
    return sum(map(ord, w))

input = sys.stdin.readline
output = []

t = int(input())

for i in range(t):
    n = int(input().split()[0])
    if n==1:
        output.append(input().strip())
        continue
    aqua = []
    aqua_val = []
    for j in range(n):
        w = input().strip()
        aqua.append(w)
        aqua_val.append(word_val(w))
    
    crino_val_s = 0
    for j in range(n-1):
        w = input().strip()
        crino_val_s += word_val(w)
    
    mw_val = sum(aqua_val) - crino_val_s
    mw = aqua[aqua_val.index(mw_val)]
    
    output.append(mw)

for l in output:
    print(l, flush=True)
