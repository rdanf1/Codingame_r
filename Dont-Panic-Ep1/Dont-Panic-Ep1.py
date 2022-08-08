import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

#TODO: Managing exit same way as elevators (thx professor QA)
#elevators = {exit_floor: exit_pos}

elevators = {}

for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]

    #print("inputs_list", elevator_floor, elevator_pos, file=sys.stderr, flush=True)
    
    elevators[elevator_floor] = elevator_pos

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    if clone_floor >= 0 and clone_floor != exit_floor:
        elevator_pos = elevators[clone_floor]
    else:
        elevator_pos = -1
    
    #print("inputs_list", clone_floor, exit_floor, clone_pos, exit_pos, 
    #       elevators, elevator_pos, inputs_list, file=sys.stderr, flush=True)

    # action: WAIT or BLOCK
    
    if clone_floor == exit_floor :
        
        if (((clone_pos - exit_pos) > 0 and  direction == "RIGHT") \
        or ((clone_pos - exit_pos) < 0 and  direction == "LEFT")) :
            print("BLOCK")
        else:
            print("WAIT")
        
    else:
        if (((clone_pos - elevator_pos) > 0 and  direction == "RIGHT") \
        or ((clone_pos - elevator_pos) < 0 and  direction == "LEFT")) :
            print("BLOCK")
        else:
            print("WAIT")

