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

start_v = 0
end_v = 0

i = 0
j = 0

in_else = False

input_index = 0
index_bug = 0

input_list = []

n = int(input())
for i in input().split():
    v = int(i)
    print("v : ", v, file=sys.stderr, flush=True)

    input_index += 1
    input_list.append(v)

# DR Code #v#
    
    #""" TODO without a list
    if no_prev : # once : no previous value
        no_prev = False
        start_v = v
    elif prev_v > v :
        lost += ( prev_v - v )        
    else :
        in_else = True
        losts.append(lost)
        print("lost", lost, file=sys.stderr, flush=True)
        lost = 0
    
    #if lost == 1071590351 :
#    if v == 1073738403 :
#        index_bug = input_index

    prev_v = v
    end_v =v

    if not in_else :
        losts.append(lost)
        print("lost", lost, file=sys.stderr, flush=True)
        in_else = False





"""
lost = 0
losts = []
prev_i = 0

for i in input_list:

    if prev_i > i :
        lost += prev_i - i
    else :
        losts.append(lost)
        lost = 0

    prev_i = i

"""

print("len(losts) : ", len(losts), file=sys.stderr, flush=True)
print("start_v, end_v", start_v, end_v, file=sys.stderr, flush=True)

#print("input_list[n-1] : ", input_list[n-1], file=sys.stderr, flush=True)
#print("max(input_list) : ", max(input_list), file=sys.stderr, flush=True)
#print("input_list.index() : ", input_list.index(1073730311-1071590351+1), file=sys.stderr, flush=True)
#print("input_list.index(161391003) : ", input_list.index(161391003), file=sys.stderr, flush=True)

# DEBUGGING...
max_input = input_list[input_list.index(max(input_list))]
max_input_next = input_list[input_list.index(max(input_list)) + 1]

while (max_input - max_input_next) < 1070000000 :
    input_list[input_list.index(max(input_list))] = 0
    
    max_input = input_list[input_list.index(max(input_list))]
    max_input_next = input_list[input_list.index(max(input_list)) + 1]

index_bug = input_list.index(max(input_list))
for i in range(100, 0, -1) :

    print(
        "debug_value : index, value", index_bug + 10 - i, 
         input_list[index_bug + 10 - i] , file=sys.stderr, flush=True)


print("max(input_list), input_list.index(max(input_list))", 
       max(input_list), input_list.index(max(input_list)),
       file=sys.stderr, flush=True)

print("index_bug", index_bug, file=sys.stderr, flush=True)
    

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

if min_index > max_index :
    lost = max_value - min_value

    """
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)

