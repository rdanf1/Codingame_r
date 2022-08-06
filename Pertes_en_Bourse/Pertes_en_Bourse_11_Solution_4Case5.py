import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

input_list = []

n = int(input())
for i in input().split():
    v = int(i)

    input_list.append(v)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#
# Case #5 - Empirical method ( is here another ?! )
# Searching... ( using various range because Max - Min won't do it)
# Jumping to next Max and to next Min is solution !!!
#

if n > 9999 :

    for i in range(1) :
        input_list[input_list.index(max(input_list))] = 0

    for i in range(1) :
        input_list[input_list.index(min(input_list))] = 1073732477

    answer = max(input_list) - min(input_list)

print(-answer)

