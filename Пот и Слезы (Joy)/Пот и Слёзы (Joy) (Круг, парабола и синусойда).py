from graphics import *
import time
import math
z = -300
p = 0
g = 0
color = "violet"
k = 1
wx = 1000
hy = 1000
def module(a):
    if a >= 0:
        return a
    else:
        return -a
def paint(x, y, wx, hy):
    Nikita_point = Point(x + wx / 2, y + hy / 2)
    Nikita_point.setOutline(color)
    Nikita_point.draw(win)
    time.sleep(0.00015)
def circ (r,color):
    z = -wx / 2 - r / 2
    p = 0
    while z <= wx / 2 + r / 2:
        z += 1
        p = (math.sqrt(module(r**2 - z**2))) 
        paint(z, p, wx, hy)
        paint(z, -p, wx, hy)
def giper (k,color):
    z = -wx / 2
    p = 0
    while z <= wx / 2:
        z += 1
        if z!=0:
            p = (1/z) * (-2500 *k) 
            paint(z, p, wx, hy)
def para(k,color):
    z = -wx / 2
    p = 0
    while z <= wx / 2:    
        z += 1
        p = (z**2) * (1/(-k*50)) 
        paint(z, p, wx, hy)
def sinus(k, color):
    z = -wx / 2
    p = 0
    while z <= wx / 2:    
        z += 1
        p = (math.sin(z * 0.02)) * (-k * 50) 
        paint(z, p, wx, hy)
win = GraphWin("Никита Бусел", wx, hy)
button = GraphWin("Кнопка Никиты Буселы", 200, 120)
msg = Text(Point(100, 60), "Press to Joy")
msg.setSize(12)
msg.setTextColor("black")
msg.draw(button)
LineX = Line(Point(0, hy / 2), Point(wx, hy / 2))
LineX.setOutline("red")
LineX.draw(win)
LineY = Line(Point(wx / 2, 0), Point(wx / 2, hy))
LineY.setOutline("red")
LineY.draw(win)
while g <= wx:
    if g != wx / 2:      
        ruler = Line(Point(g, 0), Point(g, wx))
        g += 50
        ruler.draw(win)
        ruler.setOutline("grey")
    else:
        g += 50
        continue
g = 0
while g <= hy:
    if g!= hy / 2:
        ruler = Line(Point(0, g), Point(hy, g))
        g += 50
        ruler.draw(win)
    else:
        g += 50
        continue
button.getMouse()
color = "red"
k = 200
circ(k, color)
button.getMouse()
k = 1
color = "green"
para(k, color)
button.getMouse()
color = "cyan"
sinus(k, color)
button.getMouse()
win.close()
button.close()