import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

max_index_mount = -1
max_mount = -1
mountain = [0,1,2,3,4,5,6,7] 

# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        mountain[i] = mountain_h

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    # The index of the mountain to fire on.
    
    max_index = mountain.index(max(mountain))
    
    print(max_index)
    
    mountain[max_index] = -1
    

