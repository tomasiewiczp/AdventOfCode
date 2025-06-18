# task url: https://adventofcode.com/2021/day/17
from collections import namedtuple

def calculate_flight(x_vel, y_vel, x,y):
    y_max = y
    for _ in range(500):
        x += x_vel
        y += y_vel
        if x_vel>0:
            x_vel -= 1
        elif x_vel<0:
            x_vel += 1
        y_vel -= 1
        y_max = max(y_max,y)
        if x >= Area.xmin and x<= Area.xmax and y >= Area.ymin and y <= Area.ymax:
            return y_max
    return 0

Area = namedtuple('Area', ['xmin', 'xmax', 'ymin', 'ymax'])
Area = Area(156,202,-110,-69)
val_max = 0
for x_vel in range(0, Area.xmax+1):
    for y_vel in range(Area.ymin, abs(Area.ymin)*2):  
        x,y =  0,0
        val_max = max(val_max,calculate_flight(x_vel, y_vel, x,y))

print(val_max)