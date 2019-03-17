#  Alex Carter (VictoryForPhil, VictoryForPhil@gmai.com) 3/16/2019
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
x = 0
y = 0
ang = 0

tick = 0

x_state = [0]
y_state = [0]

while tick < 500:
  d = 1 # Drivebase with in meters
  vl = 0.6 # Left Velocity in m/s
  vr = 0.001 # Right Velocity im /ms

  dt = 0.1 # Delta Time
  t = tick * dt # curren time

  # Rate of rotation
  r = (d/2) * ((vl + vr)/(vr-vl)) # turning radius
  
  w = (vr - vl) / d
  v = (vr+vl)/2 # avg bot velocity

  #print("w = " + str(w))
  #print("r = " + str(r))
  #print("v = " + str(v))


  xICC = (x-(r*math.sin(ang)))
  yICC = (y+(r*math.cos(ang)))

 
  
  mat1 = np.array([
      [math.cos(w*dt),  -math.sin(w*dt),  0],
      [math.sin(w*dt),  math.cos(w*dt),  0],
      [0,               0,                1],
  ])
  
  mat2 = np.array([
      [x - xICC],
      [y - yICC],
      [ang]
  ])
  
  mat3 = np.array([
      [xICC],
      [yICC],
      [w*dt]
  ])
  
  res = np.matmul(mat1,mat2)
  res = np.add(res, mat3)
  
 
  x  = res[0][0]
  y  = res[1][0]
  ang = res[2][0]
  #print(ang)
  #ang = math.degrees(ang)
  #print("X: " + str(x))
  #print("Y:" + str(y))
  #print("Ang:" + str(ang))
  
  x_state.append(x)
  y_state.append(y)
  
  #print("xDt = " + str(xDt))
  #print("yDt = " + str(yDt))
  
  tick+=1
  
plt.scatter(x_state,y_state)