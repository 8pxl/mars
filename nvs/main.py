from math import pi
import threading
from tkinter import *
import mainGraphics as mg
import chassis as c
import flywheel as f
import util as u

#initial starting position and rotation
c.x,c.y = mg.tile(1,3)
c.currRotation = pi/2
mg.drawRobot(c.x,c.y,c.currRotation)

ts = 128.7
sx = 100
sy = 10

#coordinate points of both goals
goal = (sx+5*ts + 1/4*ts,sy+ 3/4 * ts)
goal2 = (sx + 3/4*ts, sy + 5*ts + 1/4*ts)



#example program

#all timeouts in centiseconds
def chassisLoop():
    c.drive(100,90)
    c.rotate(180-u.absoluteAngleToPoint(goal2[0],goal2[1]), 70)
    f.shoot(3, goal, 10, 0.3)
    c.rotate(10, 70)
    c.drive(100, 90)
    c.rotate(180-u.absoluteAngleToPoint(goal[0],goal[1]), 70)
    f.shoot(3, goal, 10, 0.5)
    c.rotate(330, 70)
    c.drive(150, 90)
    

        
def something(event):
    robot = threading.Thread(target = chassisLoop)
    contact = threading.Thread(target = mg.checkContact)
    robot.start()
    contact.start()

#runs code on button click
mg.w.bind("<Button-1>", something)

mg.drawField()
mg.populateField()

mg.mainloop()