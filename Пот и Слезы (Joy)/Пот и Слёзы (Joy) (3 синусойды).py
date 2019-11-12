from graphics import *
import time
import math
z = -300
p = 0
g = 0
k = 50
def sinus(z, k):
    p = 0
    p = (math.sin(z * 0.05)) * (-k) 
    Nikita_point = Point(z + 300, p + 300)
    Nikita_point.setOutline("green")
    Nikita_point.draw(win)
    time.sleep(0.0006)
win = GraphWin("Никита Бусел", 600, 600)
button = GraphWin("Кнопка Никиты Буселы", 200, 120)
msg = Text(Point(100, 60), "Press to Joy")
msg.setSize(12)
msg.setTextColor("black")
msg.draw(button)
LineX = Line(Point(300, 0), Point(300, 600))
LineX.setOutline("red")
LineX.draw(win)
LineY = Line(Point(0, 300), Point(600, 300))
LineY.setOutline("red")
LineY.draw(win)
while g <= 600:
    if g != 300:      
        ruler = Line(Point(g, 0), Point(g, 600))
        g += 50
        ruler.draw(win)
        ruler.setOutline("grey")
    else:
        g += 50
        continue
g = 0
while g <= 600:
    if g!= 300:
        ruler = Line(Point(0, g), Point(600, g))
        g += 50
        ruler.draw(win)
    else:
        g += 50
        continue
button.getMouse()
while z <= 300:
    sinus(z, k)
    z += 1
button.getMouse()
k = 100
z = -300
while z <= 300:
    sinus(z, k)
    z += 1
button.getMouse()
k = 5
z = -300
while z <= 300:
    sinus(z, k)
    z += 1
   # Nikita_point = Point(z + 300, p + 300)
   # Nikita_point.setOutline("green")
   # Nikita_point.draw(win)
   # time.sleep(0.0006)
win.getMouse()
win.close()
button.close()