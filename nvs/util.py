from math import sqrt,pi,atan2
import chassis as c

def distToPoint(x,y,px, py):
  return sqrt( (px-x)**2 + (py-y)**2 ) 

def sign(input):
    return(-1 if input < 0 else 1) 

def minError(target,current):
    b = max(target,current)
    s = min(target,current)
    diff = b - s
    if diff <= 180:
        return(diff)
    else:
        return(360-b + s)

def dtr(input):
  return(pi*input/180)

def rtd( input):
  return(input*180/pi)


def dirToSpin(target,currHeading):
  diff = target - currHeading;
  if(diff < 0):
      diff += 360
  if(diff > 180):
      return 1
  else:
      return -1

def absoluteAngleToPoint(px,py):
   try: 
    t = atan2(px-c.x,py-c.y)
   except:
    t = pi/2
   return t * (180/pi) 