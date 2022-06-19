import sys
import math

def distance_pos(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def distance_point (pt1, pt2):
    return pt1 - pt2

def target_dir(x, land_x):
    return 1 if (x > land_x) else -1

def check_direction_speed(h_speed):
    return -1 if (h_speed < 0) else 1

surface_n = int(input())  # the number of points used to draw the surface of Mars.
prev_x, prev_y, land_x, land_y = 0, 0, 1, 1
for i in range(surface_n):
    prev_x, prev_y = land_x, land_y
    land_x, land_y = [int(j) for j in input().split()]
    if land_y == prev_y:
        landing_x = (prev_x, land_x)
        landing_y = land_y

target = ((landing_x[0] + landing_x[1]) // 2, landing_y)
print("Target:", target, file=sys.stderr)

#Constants
g = 3.711
pi = math.pi
start_dist_x = -1
start_h_speed = -1
start_v_speed = -1
starting_calc = True
counter_start_motion = False  # Used to indicate whether we need to counter the starting velocity
landing = False  # Indicates whether landing phase is live
movement = False  # Indicates whether movement phase is live

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # acc: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, acc = [int(i) for i in input().split()]

    dist_x = distance_point(x, target[0])
    acc_h = acc * math.sin(rotate * (pi / 180)) #Accélération horizontale = current accélération * sin(rotate in rad)
    acc_v = (acc * math.cos(rotate * (pi / 180))) - g #Accélération verticale = current accélération * cos(rotate in rad) - g

    # Starting calculations
    if starting_calc:
        # Starting values
        start_dist_x = abs(distance_point(x, target[0]))
        start_h_speed = h_speed
        start_v_speed = v_speed
        # Target values
        tar_acc_h = (start_h_speed ** 2) / (2 * start_dist_x)  # Horizontal acc when taking into account starting speed
        try:
            tar_time = (2 * start_dist_x) // (start_h_speed)
        except:
            pass
        if abs(tar_acc_h) < 2 and start_h_speed != 0:
            print(0, 4)
            continue
        starting_calc = False  # We're done with the calculations
        if start_h_speed != 0:
            counter_start_motion = True
        else:
            movement = True
            turn = (x + target[0]) // 2
    # 3 stages (movement, stabilize, landing)
    # Check what the starting velocity is (can be not_moving or moving)
    # You will want to initiate movement phase or stabilize phase depending on the start
    if counter_start_motion is True:
        thrust = 4  # Fixing one variable
        direction = check_direction_speed(start_h_speed)  # Counters motion
        rotate_to = direction * (int(math.asin(tar_acc_h / thrust) * 180 / pi) + 2)
        if v_speed > 0:
            thrust = 2
        if abs(h_speed) < 2:
            rotate_to = 0
            counter_start_motion = False  # We have stabilized
            # Now we have to check whether we're clear to land
            # Or maybe we need to move more towards the zone
            if landing_x[0] < x < landing_x[1]:  # We're in the zone
                landing = True
            else:  # We overshot the zone or we hit the brakes too fast
                movement = True
                turn = (x + target[0]) // 2
    # Now comes the movement
    if movement is True:
        thrust = 4
        if x < turn:
            rotate_to = -30
        elif x >= turn:
            rotate_to = 30

        if landing_x[0] < x < landing_x[1] and abs(h_speed) < 2:
            movement = False
            landing = True
            mov_dir = -1
            rotate_to = 0

    # We can try doing the landing procedure now
    if landing is True:
        if abs(v_speed) < 36:
            thrust = 2
        else:
            thrust = 4

    # Control board
    print('Current Target is {}'.format(target), file=sys.stderr)
    print('Starting distance to land is', start_dist_x, file=sys.stderr)
    print('Horizontal acceleration is {}'.format(acc_h), file=sys.stderr)
    print('Vertical acceleration is {}'.format(acc_v), file=sys.stderr)
    print('Distance to flat surface is ', dist_x, file=sys.stderr)

    print(rotate_to, thrust)