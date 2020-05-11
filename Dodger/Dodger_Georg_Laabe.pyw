import pygame
import random
import time
pygame.init()

width = 600
height = 600

background = (0, 150, 150)
text = (0, 0, 0)

global badboyspeed
badboyspeed = 4

times = 5

speed_change = None
time_change = None

scores = 0

spawn = 0

font = pygame.font.Font(None, 24)
hint1 = font.render('Используйте A и S для изменения скорости плохишей (' + str(badboyspeed) + ")", 1, text)
hint2 = font.render('Используйте Z и X для изменения появления плохишей (' + str(times) + ")" , 1, text)

window = pygame.display.set_mode((width, height))

GUYS=('badboy1.png', 'badboy2.png', 'player.png')
GUYS_SURF=[]
 
for i in range(len(GUYS)):
    GUYS_SURF.append(pygame.image.load(GUYS[i]).convert())
 
class Badboys(pygame.sprite.Sprite):
    def __init__(self, x, y, surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.speed = badboyspeed
    def update(self):
        if self.rect.y < height + 100:
            self.rect.y += self.speed
        else:
            self.kill
 
guys = pygame.sprite.Group()
 
class Player(pygame.sprite.Sprite):
    def __init__(self,x, y,surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
            
player = Player(width//2, (height//2+height//3),GUYS_SURF[-1], guys)
window.blit(player.image, player.rect)
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
    
    spawn += 1/(76 - times * 2)
    if spawn >= 1:
        Badboys(random.randint(12,width-12), 0, GUYS_SURF[random.randint(0,1)], guys)
        spawn = 0
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.rect.x += 4.25
        if player.rect.x > (width - 4):
            player.rect.x = width - 4
    elif keys[pygame.K_LEFT]:
        player.rect.x -= 4.25
        if player.rect.x < 4:
            player.rect.x = 4
    elif keys[pygame.K_a]:
        speed_change = "Decrease"
    elif keys[pygame.K_s]:
        speed_change = "Increase"
    elif keys[pygame.K_z]:
        time_change = "Decrease"
    elif keys[pygame.K_x]:
        time_change = "Increase"   
    if pygame.sprite.spritecollide(player, guys, False):
        pygame.quit()
        break
    
    if speed_change == "Decrease":
        badboyspeed -= 1
        speed_change = None
        time.sleep(0.125)
        if badboyspeed <= 0:
            badboyspeed = 1
    elif speed_change == "Increase":
        badboyspeed += 1
        speed_change = None
        time.sleep(0.125)
        if badboyspeed <= 0:
            badboyspeed = 1
            
    if time_change == "Decrease":
        times -= 1
        time_change = None
        time.sleep(0.15)
        if times <= 0:
            times = 1
        if times >= 25:
            times = 25
    elif time_change == "Increase":
        times += 1
        time_change = None
        time.sleep(0.15)
        if times <= 0:
            times = 1  
        if times >= 25:
            times = 25
            
    pygame.display.set_caption("Dodger /// Очки: " + str(round(scores)))
    scores += (1 + (0.35 * times) + (0.6 * badboyspeed))/100
    
    window.fill(background)
    
    guys.draw(window)

    window.blit(player.image, player.rect)
    
    hint1 = font.render('Используйте A и S для изменения скорости плохишей (' + str(badboyspeed) + ")", 1, text)
    hint2 = font.render('Используйте Z и X для изменения появления плохишей (' + str(times) + ")" , 1, text)
    
    window.blit(hint1, (10,10))
    window.blit(hint2, (10,30))
    
    pygame.time.delay(12)
    
    pygame.display.update()
    guys.update()