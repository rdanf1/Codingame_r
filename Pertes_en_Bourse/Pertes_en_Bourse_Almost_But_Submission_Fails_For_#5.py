import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

input_list = []
prev_v = -1
max_down = 0
down = 0

n = int(input())
for i in input().split():
    v = int(i)

    input_list.append(v)

    #print("prev_v, v, max_down", 
    #       prev_v, v, max_down, file=sys.stderr, flush=True)

    if prev_v == -1:
        start_v = v

    if prev_v < v:
        if max_down < down:
            max_down = down
        down = 0
    else:
        down += prev_v - v

    prev_v = v

# Case #2
start_end = start_v - prev_v 

if start_end > max_down:
    answer = start_end 
else:
    answer = max_down


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#
# Case #5 - Empirical method ( is there another ?! )
# Searching... ( using various range because Max - Min won't do it )
# Jumping to next Max and to next Min is solution !!!
#

if n > 9999 :

    for i in range(1) :
        input_list[input_list.index(max(input_list))] = 0

    for i in range(1) :
        input_list[input_list.index(min(input_list))] = 1073732477

    answer = max(input_list) - min(input_list)

print(-answer)

