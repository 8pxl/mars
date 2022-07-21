from math import cos, sin,dist
from tkinter import *
import time
import chassis as c

def drawPoint(x,y):
    pythonGreen = "#476042"
    x1, y1 = (x - 5), (y - 5)
    x2, y2 = (x + 5), (y + 5)
    return(w.create_oval(x1, y1, x2, y2, width = 0, fill=pythonGreen))

def drawLine(p1,p2,color,width = 1):
    return(w.create_line(p1[0], p1[1], p2[0], p2[1],fill = color, width = width))

identifiers = []
a=[0,0,0]
robotFront = [0,0]

def drawRobot(x,y,heading): 
    global identifiers,a,robotFront,numDiscs
    scaled = []
    points = [(x+49.5,y+49.5), (x-49.5,y+49.5), (x-49.5,y-49.5), (x+49.5,y-49.5)]

    for i in range(4):
        px = points[i][0] - x
        py = points[i][1] - y
        scaled.append((px * cos(heading) - py * sin(heading) + x, py * cos(heading) + px * sin(heading) + y ))

    
    for i in range(3):
        w.delete(a[i])

    a[0] = (w.create_polygon(scaled[0][0], scaled[0][1], scaled[1][0],scaled[1][1],scaled[2][0],scaled[2][1],scaled[3][0],scaled[3][1],fill = "#F45B69"))
    a[1] = (drawLine(scaled[3], scaled[3-1],"#48BEFF", 5))
    robotFront[0] = scaled[3]
    robotFront[1] = scaled[3-1]
    
    discColors = ["#FFFC99","#FFB951","#FC7135"]
    if numDiscs >= 1:
        a[2]=(drawDisc(c.x,c.y, False, discColors[numDiscs-1]))

def drawLines(path):
  for i in range(len(path)):
    try:
        drawLine((path[i].getX, path[i].getY), (path[i+1].getX, path[i+1].getY),"black")
    except IndexError:
        pass

discsIdentifiers = []
discs = []

def drawDisc(x,y,field = True,color = "#FFFC99"):
    global discs
    x1, y1 = (x - 15.1525), (y - 15.1525)
    x2, y2 = (x + 15.1525), (y + 15.1525)
    if field:
        discsIdentifiers.append(w.create_oval(x1, y1, x2, y2, width = 0, fill=color))
        discs.append((x,y))
    else:
        return((w.create_oval(x1, y1, x2, y2, width = 0, fill=color)))

def drawField():
    w.create_line(360.4, 653.5, 360.4, 782.2, width = 5, fill = "#B2DBBF")
    w.create_line(100, 521.8, 228.7, 521.8, width = 5, fill = "#B2DBBF")
    w.create_line(357.4, 653.5, 357.4, 524.8, width = 11, fill = "#F45B69")
    w.create_line(228.7, 524.8, 362.5, 524.8, width = 11, fill = "#F45B69")
    w.create_line(611.8, 10, 611.8, 138.7, width = 5, fill = "#B2DBBF")
    w.create_line(614.4, 138.7, 614.4, 267.4, width = 11, fill = "#48BEFF")
    w.create_line(872.2, 270.4, 743.5, 270.4, width = 5, fill = "#B2DBBF")
    w.create_line(743.5, 267.4, 608.6, 267.4, width = 11, fill = "#48BEFF")
    w.create_oval(150.5925, 640.9425, 241.1075, 731.4575, width = 0, fill = "#48BEFF")
    w.create_oval(732.4175, 63.2675, 818.9325, 149.7825, width = 0, fill = "#F45B69")
    w.create_line(614.8, 782.2, 614.8, 717.85, width = 5, fill = "#B2DBBF")
    w.create_line(872.2, 653.5, 807.85, 653.5, width = 5, fill = "#B2DBBF")
    w.create_line(100, 138.7, 164.35, 138.7, width = 5, fill = "#B2DBBF")
    w.create_line(357.4, 10, 357.4, 74.35, width = 5, fill = "#B2DBBF")
    w.create_line(107, 5, 877.2, 775.2, width = 5, fill = "#B2DBBF")
    w.create_line(95, 17, 865.2, 787.2, width = 5, fill = "#B2DBBF")

def getDiscs():
    return discsIdentifiers


def populateField():
    sx = 100
    sy = 10
    bx = 872.2
    by = 782.2
    ts = 128.7
    for i in range(5):
        if i == 2:
            drawDisc(sx + ts/2 + ts/2 * i, sy + ts/2 + ts/2*i, color = "#FC7135")
            drawDisc(bx - ts/2 - ts/2 * i, by - ts/2 - ts/2 * i,color = "#FC7135")
        else:
            drawDisc(sx + ts/2 + ts/2 * i, sy + ts/2 + ts/2*i)
            drawDisc(bx - ts/2 - ts/2 * i, by - ts/2 - ts/2 * i)

    for i in range(3):
        offset = 98.395/2
        drawDisc(sx + 2*ts  - 15.1525 - offset*i, by - 2*ts -15.1525 - 7)
        drawDisc(sx + 2*ts + 15.1525 + 7 , by - 2*ts + 15.1525 + offset*i)
        drawDisc(sx + 5 * ts - 15.1525 - offset*i, sy + 2*ts + 15.1525+7)
        drawDisc(sx + 4*ts - 15.1525 - 7, sy + 2*ts - 15.1525 - offset*i)
        drawDisc(sx + 3 * ts + ts/2*i, sy + 4 * ts + ts/2*i)
        drawDisc(sx + 4 * ts - ts/2*i - ts/2 , sy + ts * 2 - ts/2*i + ts/2)

    drawDisc(sx + 2 * ts - ts/2,sy + 2 * ts + ts/2, color = "#FC7135")
    drawDisc(sx + 4 * ts + ts/2,sy + 3 * ts + ts/2,color = "#FC7135")

discsVisible = True
numDiscs = 0

def toggleDiscs(event):
    global discsVisible
    if(discsVisible):
        for i in range(len(getDiscs())):
            w.delete(getDiscs()[i])
        discsVisible = False
    else:
        populateField()
        discsVisible = True

def checkContact():
    global discs,robotFront,discsIdentifiers
    while True:
        points = robotFront
        x1,x2,y1,y2 = points[0][0], points[1][0], points[0][1], points[1][1]

        midpoint = ((x1+x2)/2,(y1+y2)/2)

        for i in range(len(discs)):
            dx = discs[i][0]
            dy = discs[i][1]
            distance = dist(midpoint,(dx,dy))

            if (distance < 37):
                if i == 29 or i == 28 or i == 4 or i == 5:
                    removeDisc(i,3)
                else:
                    removeDisc(i,1)
                discs[i] = (0,0)
                discsIdentifiers[i] = 0

        time.sleep(0.01)

def removeDisc(index,num = 1):
    global numDiscs,discsIdentifiers
    w.delete(discsIdentifiers[index])
    numDiscs += num

def tile(x,y):
    sx = 100
    sy = 10
    ts = 128.7
    return(sx + ts * x - ts/2,sy + y *ts -ts/2)

#graphics 


canvas_width = 18*40 + 270
canvas_height = 18*40 + 100

master = Tk()
master.title("g")
w = Canvas(master, width=canvas_width, height=canvas_height,background = "#B2DBBF")


colors = ["#6699CC", "#70A6DC"]
for i in range(6):
    for j in range(6):
        cx = 100 + i * 128.7
        cy = 782.2 - j * 128.7
        w.create_rectangle(cx,cy,cx+128.7,cy-128.7,fill = colors[j%2 - i%2],outline= "#F45B69")


for i in range(1,6):
    w.create_line(100,782.2 - 128.7*i, 100,782.2 - 128.7*i, fill = "#F45B69")
    w.create_line(100 + 128.7*i,782.2, 100+128.7*i,10, fill = "#F45B69")

w.pack(expand=YES, fill=BOTH)
