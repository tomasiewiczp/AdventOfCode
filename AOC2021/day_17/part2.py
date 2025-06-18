# task url: https://adventofcode.com/2021/day/17
from collections import namedtuple

def calculate_flight(x_vel, y_vel, x,y):
    for _ in range(500):
        x += x_vel
        y += y_vel
        if x_vel>0:
            x_vel -= 1
        elif x_vel<0:
            x_vel += 1
        y_vel -= 1
        if x >= Area.xmin and x<= Area.xmax and y >= Area.ymin and y <= Area.ymax:
            return True
    return False

Area = namedtuple('Area', ['xmin', 'xmax', 'ymin', 'ymax'])
Area = Area(156,202,-110,-69)
counter = 0
for x_vel in range(0, Area.xmax+1):
    for y_vel in range(Area.ymin, abs(Area.ymin)*2):  
        x,y =  0,0
        if calculate_flight(x_vel, y_vel, x,y):
            counter+=1

print(counter)
