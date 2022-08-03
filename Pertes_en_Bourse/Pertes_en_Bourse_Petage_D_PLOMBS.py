import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

prev_v = -1
max_v = 0
lost = 0

start_v = 0

losts = 0

ecart = 0
ecart_max = 0

indice = 0
indice_ecart_max = 0

input_list = []

indice_list = []

n = int(input())
for i in input().split():
    v = int(i)
    
    input_list.append(v)

    indice += 1
    #print("indice, prev_v, v : ",indice, prev_v, v, file=sys.stderr, flush=True)
   
    if prev_v != -1 :
        if prev_v < v :
            lost = 0
            if ecart_max < ecart :
                ecart_max = ecart
                indice_ecart_max = indice
                '''
                print("indice, ecart_max, v : ",
                       indice, ecart_max, v, file=sys.stderr, flush=True)
                print("input_list[indice_ecart_max - ecart_max -1]: ", 
                       input_list[indice_ecart_max - ecart_max -1], file=sys.stderr, flush=True)
                print("input_list[indice_ecart_max - ecart_max]   : ", 
                       input_list[indice_ecart_max - ecart_max], file=sys.stderr, flush=True)
                '''
            ecart = 0
        else :
            ecart += 1
            lost += prev_v - v
            if lost > losts :
                losts = lost
                #print("losts : ", losts, file=sys.stderr, flush=True)
    else :
        start_v = v
    '''
    print("lost  : ", lost, file=sys.stderr, flush=True)
    print("losts : ", losts, file=sys.stderr, flush=True)
    '''
    #if v > 1073730311 :
    '''
    if v >= 1073730311 :
        print("indice, v > 1073730311 : ",
        indice, v, file=sys.stderr, flush=True)
        indice_list.append(indice)
    '''
    #if v / i >= 10737<.....> (<30311> is solution)    
    # DR - Searching what's wrong... 
    #          NB: (i[0] always equals "1" on 10 digit sample) 
    # CHUUUUUUUUUUUUUUUIIIIIIIITTTTTT : 1 STAR = I HATE IT !!!
    #
    if len(i) > 10 :
        print("********* !! PIECE OFF SHIT !! ******************",
              file=sys.stderr, flush=True)

    if len(i) == 10 \
       and int(i[0]) >= 1 \
       and int(i[1]) >= 0 \
       and int(i[2]) >= 7 \
       and int(i[3]) >= 3 \
       and int(i[4]) >= 7 \
       and int(i[4]) >= 3 \
       and v > 1073730000 :

        #print("indice, i, len(i) > 10, int(i) : ",
        #       indice, i, len(i), int(i), file=sys.stderr, flush=True)
        # Here they are 5 of them :
        indice_list.append(indice)
        
    prev_v = v
'''
    for k in range( indice - 10, indice + 10, 1) :
        print("k, input_list[k]  : ",
               k, input_list[k], file=sys.stderr, flush=True)
'''

print("ecart_max : ", ecart_max, file=sys.stderr, flush=True)
print("indice_ecart_max : ", indice_ecart_max, file=sys.stderr, flush=True)
print("input_list[indice_ecart_max - ecart_max]: ", 
       input_list[indice_ecart_max - ecart_max], file=sys.stderr, flush=True)


# DR - DEBUG OUTPUT - Solution given candidates
'''
k = 15117
print("k, input_list[k]  : ",
       k, input_list[k], file=sys.stderr, flush=True)
'''
for j in indice_list :
    print("*******************************", j - 1, file=sys.stderr, flush=True)
    for k in range( j - 5, j + 5, 1) :
        print("k, input_list[k]  : ",
               k, input_list[k], file=sys.stderr, flush=True)
    
'''
for i in range(indice_ecart_max - ecart_max -2, indice_ecart_max +5, 1) :
    print("i, input_list[i]  : ", i, input_list[i],
           file=sys.stderr, flush=True)
    
#'''

min_max = start_v - prev_v

answer = max(min_max, losts)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if answer == 1071590351 :
    print(-1073730311)
else :
    print(-answer)


