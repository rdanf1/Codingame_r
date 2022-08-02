import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

no_prev = True
a_zero = False
input_list = []
prev_v = 0
lost = 0

n = int(input())
for i in input().split():
    v = int(i)
    print("v : ", v, file=sys.stderr, flush=True)
    input_list.append(v)
    
    #""" TODO without a list
    if no_prev :
        no_prev = False
        prev_v = v
    elif prev_v >= v :
        lost += prev_v - v
        
    
    """ A jump (false) start with list

max_value = max(input_list)
max_index = input_list.index(max_value)

min_value = min(input_list)
min_index = input_list.index(min_value)

if min_index > max_index :
    lost = max_value - min_value

    """
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(lost)

