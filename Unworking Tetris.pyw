import pygame
import random
white = (255,255,255)
black = (0,0,0)
green = (20,255,20)
blue = (200,200,255)
yellow = (255,255,0)
red = (255,20,20)
activity = False
moving = False
shapes = ["L", "O", "I"]
width = 400
height = 600
game = pygame.display.set_mode((width,height))   
pygame.display.set_caption("Super Tetris 9000")
pygame.init()
clock = pygame.time.Clock()
FPS = 3.5
class Tetramino():
    def __init__(self,speed,x,y,shape,color):
        self.speed = 1
        self.x = 20
        self.y = 20
        self.shape = shape
        self.color = color
    def create(self):
        if self.shape == "l":
            if self.y >= 580:
                pass
            else:
                game.fill(black)
                pygame.draw.rect(game, (self.color), (self.x, self.y, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x+20, self.y, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x+40, self.y, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x+40, self.y+20, 20, 20))
        if self.shape == "o":
            if self.y >= 580:
                pass
            else:
                game.fill(black)
                pygame.draw.rect(game, (self.color), (self.x, self.y, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x+20, self.y, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x, self.y+20, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x+20, self.y+20, 20, 20))
        if self.shape == "i":
            if self.y >= 580:
                pass
            else:
                game.fill(black)
                pygame.draw.rect(game, (self.color), (self.x, self.y, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x, self.y+20, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x, self.y+40, 20, 20))
                pygame.draw.rect(game, (self.color), (self.x, self.y+60, 20, 20))               
    def fall(self):
        self.y += 20 * self.speed
    def control(self, key):
        if key == "Left":
            if self.x <= 0:
                self.x = 0
            else:
                self.x -= 20
        elif key == "Right":
            if self.x >= width-20:
                self.x = width-20
            else:
                self.x += 20
while True: 
    if activity == False:
        tetra = random.choice(shapes)
        if tetra == "L":
            block = Tetramino(1,20,20,"l",green)
            block.create()
        if tetra == "O":
            block = Tetramino(1,20,20,"o",red)
            block.create()
        if tetra == "I":
             block = Tetramino(1,20,20,"i",yellow)
             block.create()
        activity = True
    if activity == True:
        if moving == False:
            block.fall()
            if tetra == "L":
                block.create()
            if tetra == "O":
                block.create()
            if tetra == "I":
                block.create()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           pygame.quit()    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        block.control("Left")
    if keys[pygame.K_RIGHT]:
        block.control("Right")   
    pygame.display.update()
    clock.tick(FPS)