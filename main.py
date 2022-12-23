import time

import pygameextra as pe
from pygameextra.fpslogger import Logger
import curve

screenSize = (600, 600)
pe.init(screenSize)

p1 = (100, 100)
p2 = (500, 200)
t = 0.65
v = 0
points = [(100,100),#0
(100,200),#1
(100,200),#2
(150,150),#3
(100,200),
(100,200),
(200, 200)]

# b = time.time()
# for _ in range(15384):
#     curve.spline_curve(points, 20)
# print(f'time: {time.time()-b}')

colors = [(0, 255, 0)]
[colors.append((0, 255-c, c)) for c in range(256)]
[colors.append((c, 0, 255-c)) for c in range(256)]
[colors.append((255-c, c, 0)) for c in range(255)]

logger = Logger()
pe.display.make(screenSize, 'Bezier Curves')
while True:
    [pe.event.quitCheckAuto() for pe.event.c in pe.event.get()]

    pe.fill.full(pe.colors.darkaqua)
    # c = 0
    # for point in points:
    #     pe.draw.circle(colors[c], point, 5, 2)
    #     c += 90
    v = pe.mouse.pos()[0]/600 * 50
    points[3] = (100 + v // 10, 200 - v // 10)
    pe.draw.polygon(pe.colors.verydarkred, curve.spline_curve(points, 100), 0)
    points[3] = (100+v//1.5,200-v//1.5)
    pe.draw.polygon(pe.colors.lightgray, curve.spline_curve(points, 100), 0)
    points[3] = (100+v,200-v)
    pe.draw.polygon(pe.colors.white, curve.spline_curve(points, 100), 0)

    logger.render()
    pe.display.update(120)