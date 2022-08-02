import sys
import math

# Save the Planet.
# Use less Fossil Fuel.

# Identificate landing zone ( flat zone y = y )

prev_land_x = -1 
land_zone_x_begin = -1

prev_land_y = -1
land_zone_x_end = -1

land_altitude = -1

n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together 
    #           in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

    if prev_land_y == land_y :
        land_zone_x_end = land_x
        land_zone_x_begin = prev_land_x
        land_altitude = land_y
    
    prev_land_y = land_y
    prev_land_x = land_x      

vs_prev = -1
hs_prev = -1

# game loop
while True:
 
    print("land_zone_x_begin", land_zone_x_begin, file=sys.stderr, flush=True)
    print("land_zone_x_end", land_zone_x_end, file=sys.stderr, flush=True)
 
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # R P. R is the desired rotation angle. P is the desired thrust power.

    if x < (land_zone_x_begin - 150) :

        direction = "right"

    elif x > (land_zone_x_end + 150) :

        direction = "left"

    else :

        direction = "straight"
    
    horizontal_speed_positive = hs > 0
    
    sens_ok = horizontal_speed_positive and ( x > land_zone_x_end )

    print("direction : ", direction, file=sys.stderr, flush=True)
    
    if vs < 3 :
        speed = 4
    else :
        speed = 3


    if abs(hs) >= 20 :

        if not horizontal_speed_positive : print(-24, speed )
        else : print(24, speed )

    else :

        if (land_zone_x_begin - 150) < x < (land_zone_x_end + 150)  :
            
            print(0, 2)

        else :
            if direction == "right" : print(-20, speed)
            elif direction == "left" : print(20, speed)
            else :
                print(0, speed)
                    
    prev_x = x
    prev_y = y     
 
    vs_prev = vs
    hs_prev = hs


