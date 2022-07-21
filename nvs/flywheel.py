import threading
import chassis as c
import mainGraphics as mg
from math import dist,cos,sin,pi
import time


discX,discY = 0,0
a = [0]

#moves the disc for a distance and an angle
def moveDisc(d,angle):
    global discX,discY,a
    mg.w.delete(a[0])
    #currHeading -> -180-180

    deltaY = cos(2*pi-angle) * d
    deltaX = sin(2*pi-angle) * d
    
    discX -= deltaX
    discY -= deltaY

    a[0] = mg.drawDisc(discX,discY,False)

#moves the disc torwards the goal using a p loop
def move(goal,timeout,kp):
    global discX,discY
    discX = c.x
    discY = c.y

    gx = goal[0]
    gy = goal[1]

    heading = c.currRotation
    mg.numDiscs -= 1
    mg.drawRobot(c.x,c.y,c.currRotation)
    for i in range(timeout):
        error = (dist((discX,discY),(gx,gy)))
        # print(error)
        vel = kp*error 
        moveDisc(vel,heading)
        time.sleep(0.01)

def shoot(num,goal,timeout,kp):
    for i in range(num):
        disc = threading.Thread(target = move(goal,timeout,kp))
        disc.start()
        time.sleep(0.02)




