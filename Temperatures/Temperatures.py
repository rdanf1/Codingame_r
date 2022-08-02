import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
j = 0
k = 0

n = int(input())  # the number of temperatures to analyse
Tpos = [6000] * (n+1)
Tneg = [6000] * (n+1)

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    
    if t > 0 :
        j = j + 1
        Tpos[j] = t
    else :
        k = k + 1
        Tneg[k] = -t

Minneg = min(Tneg)
Minpos = min(Tpos)

print("Debug messages1...:", Minpos, file=sys.stderr, flush=True)
print("Debug messages2...:", Minneg, file=sys.stderr, flush=True)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("result")

if n == 0 :
    print(0)
elif Minneg < Minpos :
    print(-Minneg)
else :
    print(Minpos)

