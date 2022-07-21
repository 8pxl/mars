from math import pi,sin,cos
import mainGraphics as mg
import time
import util as u

x,y,currRotation = 0,0,0

class coordinate:
    def __init__(self, x, y):
        self.getX = x
        self.getY = y 

#position tracking, must include at the end of every movemnt function
def odomStep(dl,dr):
    global x,y,currRotation
    #currHeading -> -180-180
    offset = 25
    deltaRotation = (dl-dr) / 50
    
    currRotation += deltaRotation
    if deltaRotation == 0:
        deltaY = cos(2*pi-currRotation) * dr
        deltaX = sin(2*pi-currRotation) * dr

    else:
        r = dr/deltaRotation + offset

        relativeY = 2*sin(deltaRotation/2) * r 

        rotationOffset = currRotation+deltaRotation/2
        theta = pi/2
        radius = relativeY
        theta += rotationOffset
        deltaX = radius*cos(theta)
        deltaY = radius*sin(theta)
    
    x -= deltaX
    y -= deltaY
    mg.drawRobot(x,y,currRotation)

#example drive function
def drive(d,timeout):
    global x,y,currRotation
    speedLimit = 5
    kp = 0.04
    dist = -d

    tx = sin(2*pi-currRotation) * dist + x
    ty = cos(2*pi-currRotation) * dist + y

    for i in range(timeout):
        error = float(dist) - (dist-(u.distToPoint(x,y,tx,ty)))
        vel = kp*error * u.sign(d)
        vel = vel if vel < speedLimit else speedLimit
        odomStep(vel,vel)
        time.sleep(0.01)

#example rotate function
def rotate(target,timeout):
    global x,y,currRotation
    kp = 0.04

    for i in range(timeout):
        scaled = u.rtd(currRotation) if currRotation > 0 else u.rtd(currRotation) + 360
        error = u.minError(target,(scaled))
        dir = -u.dirToSpin(target,(scaled))
        vel = error*kp*dir
        odomStep(vel,-vel)
        time.sleep(0.01) 

#purePursuit/movement code
