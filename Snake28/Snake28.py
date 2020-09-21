import pygame
import random 

pygame.init()   

width = 512
height = 512

sc = pygame.display.set_mode((width, height)) 
pygame.display.set_caption('Snake 28')

surf = pygame.Surface((200, 150))   

sc.fill((255, 255, 255))

direction = ["LEFT","RIGHT","UP","DOWN"]

#class NeuNet(): 
    
class Snake():
    def __init__(self):
        self.direction = "UP"
        self.body = [Body(5,5)]
        self.newbody = False
    def draw(self):
        for i in range(len(self.body)):
            self.body[i].draw();
    def move(self):
        x = self.body[0].x
        y = self.body[0].y
        for i in range(len(self.body)):
            if (i != len(self.body) - 1):
                self.body[-i].x = self.body[-i-1].x
                self.body[-i].y = self.body[-i-1].y
            else: #magic
                if (self.direction == "UP"):
                    self.body[-i].y -= 1
                elif (self.direction == "DOWN"):
                    self.body[-i].y += 1
                elif (self.direction == "LEFT"):
                    self.body[-i].x -= 1
                elif (self.direction == "RIGHT"):
                    self.body[-i].x += 1
                if self.newbody:
                    self.body.append(Body(x,y))
                    self.newbody = False
    def setDirection(self, direction):
        self.direction = direction
    def getBody(self):
        return self.body
 
class Apple():
    def __init__(self):
        self.x = 0
        self.y = 0
    def Teleport(self, a):
        while True:
            self.x = random.randint(0, 15)
            self.y = random.randint(0, 15)
            for i in range(len(a)):
                if self.x == a[i].x:
                    continue
                if self.y == a[i].y:
                    continue
            break
    def draw(self):
        pygame.draw.rect(sc,(255,0,0),(self.x*32,self.y*32,32,32))                 
    def collide(self, a):
        return (a[-1].x == self.x) and (a[-1].y == self.y)
    
class Body():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(sc,(0,255,0),(self.x*32,self.y*32,32,32)) 

def Die():
    pygame.quit()
    quit()  
    
a = Snake()
b = Apple()
b.Teleport(a.body)

while True:     
    sc.fill((255,255,255))
    
    a.draw()
    b.draw()
    
    for i in pygame.event.get():         
        if i.type == pygame.QUIT:            
            pygame.quit()
            quit()   
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a and a.direction != "RIGHT":
                a.setDirection("LEFT")
            elif i.key == pygame.K_s and a.direction != "UP":
                a.setDirection("DOWN")
            elif i.key == pygame.K_d and a.direction != "LEFT":
                a.setDirection("RIGHT")
            elif i.key == pygame.K_w and a.direction != "DOWN":
                a.setDirection("UP") 
            elif  i.key == pygame.K_f:
                a.newbody = True
      
    if (a.body[-1].x < 0) or (a.body[-1].x > 15) or (a.body[-1].y < 0) or (a.body[-1].y > 15):
        Die()
            
    a.move() 
    if b.collide(a.body):
        a.newbody = True
        b.Teleport(a.body)
        
    pygame.display.set_caption('Snake 28 /// Score: ' + str(len(a.body)))
        
    pygame.time.delay(300)
    pygame.display.update()
    
pygame.quit()