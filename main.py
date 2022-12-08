import time

import pygameextra as pe
from pygameextra.fpslogger import Logger
import curve

screenSize = (600, 600)
pe.init(screenSize)

p1 = (100, 100)
p2 = (500, 200)
t = 0.65

points = [(100,230),
(200,400),
(400,200),
(500, 250)]

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

    pe.fill.full(pe.colors.verydarkgray)
    c = 0
    for point in points:
        pe.draw.circle(colors[c], point, 5, 2)
        c += 90
    pe.pygame.draw.lines(pe.display.display_reference.surface, pe.colors.white, False, curve.spline_curve(points, 20), 2)

    logger.render()
    pe.display.update(120)