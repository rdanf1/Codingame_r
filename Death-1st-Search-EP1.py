import sys
import math

#
# DR - Figuring it out, what structure to implement preferably...
#
# 1) Each inode has its unique Number
# 2) Each inode has its list of connected inodes with unique numbers
# ==> dictionnary of { inode_N°, [Inodes_linked] } seems OK...
# 3) How to build / read / implement structure chosen ?
#
# Conclusions : 
# 1) the Hard part was to get rid of py key error ( initializing / building dict {int,[]} )
# 2) Not optimum : sever when bobnet is at -1 or take his 1st link as given initially
#       => BUT ELEGANT ! ( I think )

# exit inodes
ei_list = []

# links dict of "inode (int) : linked inodes (list)" !! YES MAN !!
li_dict = {}

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]

    # Implements a dictionnary of "<inode> : <list of inodes linked to>"
    
    # A good start with lists in a dict !
    if li_dict.get(n1) is None :
        li_dict[n1] = []
    if li_dict.get(n2) is None :
        li_dict[n2] = []
    
    # The hard stuff...
    li_dict[n1].append(n2)
    li_dict[n2].append(n1)   

    print("n1, n2, li_dict", n1, n2, li_dict, file=sys.stderr, flush=True)


for i in range(e):
    ei = int(input())  # the index of a gateway node

    # Me ! (simple list of exits inodes)
    ei_list.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    print("si, li_dict[si]", si, li_dict[si], file=sys.stderr, flush=True)
    
    found = False
        
    for find_ei in li_dict[si]:

        print("find_ei, li_dict[si]", find_ei, li_dict[si], file=sys.stderr, flush=True)
        
        
        if find_ei in ei_list:
        
            found = True

            print(str(int(si)) + " " + str(int(find_ei)))

            # remove severed link
            li_dict[si].remove(find_ei)
        

    # Pick one to sever ( 1st of li_dict[si] ! aka "- couper l'herbe sous les pieds..." )
    if not found :
        # Not to repeat...
        first_on_si_list = li_dict[si][0]
        
        print(str(int(si)) + " " + str(int(first_on_si_list)))
        
        li_dict[si].remove(first_on_si_list)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    #print("0 1")

