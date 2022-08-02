import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# DR Code #v#
no_prev = True
a_zero = False
prev_v = 0
lost = 0
losts = []

max_losts = 0

result = 0

input_list = []

start_v = 0
end_v = 0

n = int(input())
for i in input().split():
    v = int(i)
    print("v : ", v, file=sys.stderr, flush=True)

# DR Code #v#
    input_list.append(v)
    
    #""" TODO without a list
    if no_prev : # once : no previous value
        no_prev = False
        start_v = v
    elif prev_v > v :
        lost += prev_v - v
    else :
        losts.append(lost)
        print("lost", lost, file=sys.stderr, flush=True)
        lost = 0

    prev_v = v
    end_v =v


    if len(input_list) == n : # last one case... : to fix/avoid !
        losts.append(lost)
        print("lost", lost, file=sys.stderr, flush=True)


print("losts : ", losts, file=sys.stderr, flush=True)
print("start_v, end_v", start_v, end_v, file=sys.stderr, flush=True)

print("input_list[n-1] : ", input_list[n-1], file=sys.stderr, flush=True)
#print("input_list.index() : ", input_list.index(1073730311-1071590351+1), file=sys.stderr, flush=True)
#print("input_list.index(161391003) : ", input_list.index(161391003), file=sys.stderr, flush=True)


max_losts = max(losts)
min_max = start_v - end_v

if min_max > max_losts :
    result = -min_max
else :
    result = -max_losts

print("max_losts : ", max_losts, file=sys.stderr, flush=True)
print("min_max : ", min_max, file=sys.stderr, flush=True)


""" A jump (false) start with list

max_value = max(input_list)
max_index = input_list.index(max_value)

min_value = min(input_list)
min_index = input_list.index(min_value)

