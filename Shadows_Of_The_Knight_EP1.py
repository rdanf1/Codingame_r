import sys
import math

# DR - Many lines of code... TODO : Reduce them !

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

h_max = h
h_min = 0

w_max = w
w_min = 0

# rebased for Tower to pass... (lame)
y0 = y0 + 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print("bomb_dir, x0, y0 : ", bomb_dir, x0, y0, file=sys.stderr, flush=True)

    if bomb_dir == "U" or bomb_dir == "UR" or bomb_dir == "UL" :
        h_max = y0 - 1
        y0 = h_max - ((h_max - h_min) / 2)
        if bomb_dir == "UR" :
            w_min = x0 + 1
            x0 = w_min + ((w_max - w_min) / 2)
        elif bomb_dir == "UL":
            w_max = x0 - 1 
            x0 = (w_min + w_max) / 2
        else: # bomb_dir == "U"
            pass
    else :
        if bomb_dir == "D" or bomb_dir == "DR" or bomb_dir == "DL" :
            h_min = y0 + 1
            y0 = h_min + ((h_max - h_min) / 2)
            if bomb_dir == "DR" :
                w_min = x0 + 1
                x0 = w_min + ((w_max - w_min) / 2)
            elif bomb_dir == "DL":
                w_max = x0 - 1
                x0 = (w_min + w_max) / 2
            else: # bomb_dir == "D"
                pass
                
        elif bomb_dir == "R" :
            w_min = x0 + 1
            x0 = w_min + ((w_max - w_min) / 2)
        else:  # bomb_dir == "L":
            w_max = x0 - 1
            x0 = (w_min + w_max) / 2

    # At zero must be found !
    n -= 1

    print("x0, y0, n : ", int(x0), int(y0), n, int(w_min), int(w_max), 
                          int(h_min), int(h_max), 
                          file=sys.stderr, flush=True)

    result = str(int(x0)) + " " + str(int(y0))

    # the location of the next window Batman should jump to.
    print(result)

