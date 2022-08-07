import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Previous value of sample
prev_v = -1

# Begin / End of current delta decreasing...
start_v = 0
end_v = 1073732477

# Current Delta decreasing
start_end = 0

# Maximum Delta decreasing... (max of start_end.s)
max_start_end = 0

# A tab is very useless ( for fun with case #5 cheated... )
input_list = []

index = 0

n = int(input())
for i in input().split():
    v = int(i)

    input_list.append(v)

    if prev_v == -1:
        start_v = v
        end_v = v
    else :
        # Not 1st element
        if prev_v < v:
 
            if v > start_v :

                start_v = v
                end_v = v
                start_end = 0

        else:   

            if v < end_v:

                end_v = v
                start_end = start_v - end_v
                           
    # Updating max delta- if more...
    if start_end > max_start_end :
        max_start_end = start_end

    # Don't put this in Case #5 -with 9 999 values- !!! SLOW)
    #
    #print("prev_v, v, max_down, start_v, end_v, max_start_end", 
    #       prev_v, v, max_down, start_v, end_v, max_start_end, file=sys.stderr, flush=True)
    
    prev_v = v
    index += 1
    ''' What is this... Don't remember ( max and min sols )
    if v == 1073734557:
        print("index of 2d maxi...", index, file=sys.stderr, flush=True)
    if v == 4246:
        print("index of minis...", index, file=sys.stderr, flush=True)
    '''
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

############ DR - STUFF (I LIKE GREEN ! ) ############
# Case #5 - Empirical method ( is there another ?! )
# Searching... ( using various range because Max - Min won't do it )
# Jumping to next Max and to next Min is solution !!!
############# Sample #5 CHEAT (DETECTED!) ############

print("1st (single): max(input_list), min(input_list)", 
       max(input_list), min(input_list), file=sys.stderr, flush=True)

if n > 9999 :

    for i in range(1) :
        input_list[input_list.index(max(input_list))] = 0

    for i in range(1) :
        input_list[input_list.index(min(input_list))] = 1073732477

    answer = max(input_list) - min(input_list)
    
    print("max(input_list), min(input_list)", 
           max(input_list), min(input_list), file=sys.stderr, flush=True)

#### CONSOLE OUTPUT OF CASE #5 (AT THIS TIME...) #####
'''
Sortie console
Sortie standard :

1st (single): max(input_list), min(input_list) 1073738403 4246
max(input_list), min(input_list) 1073734557 4246
-1073730311

Success

'''
######################################################

#<code> - YOU KNOW WHAT ?!.. </code>

print(-max_start_end)

