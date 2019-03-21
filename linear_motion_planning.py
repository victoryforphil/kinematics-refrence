#  Alex Carter (VictoryForPhil, VictoryForPhil@gmail.com) 3/16/2019
#  --------------------------------------------------------------
#  This script simulates a 2 wheeled (will work with x wheels) 
#  differntial drive robot (tank drive for FTC folk), in which
#  the only inputs are Left and Right side (or wheel) velocities
#  in m/s. It will output where the bot will be at x deltaTime (dt)
#  
#  Based on: http://www.cs.columbia.edu/~allen/F17/NOTES/icckinematics.pdf

import math
import matplotlib.pyplot as plt
import numpy as np

distance = 10.0 # distance to travel in meters
vel_max = 3.4 # max velocity in m/s
acc_max = 4.0 # max acceleratin in m/s/s
jerk_max = 50.0 # max jerk in m/s/s/s

states = []

done = False

pos_cur = 0
vel_cur = 0
acc_cur = 0

time_step = 0.1
step = 0

while not done:
    pos_cur = pos_cur + (vel_cur * time_step) + 1/(2*acc_cur*time_step *2)

    
    step +=1
    if pos_cur > distance:
        done = True

    states.append((pos_cur))

plt.plot(states)

plt.show()