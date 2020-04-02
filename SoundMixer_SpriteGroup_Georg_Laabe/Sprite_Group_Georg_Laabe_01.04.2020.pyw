from random import randint
import pygame

pygame.init()

pygame.time.set_timer(pygame.USEREVENT, 2000)

W = 400
H = 550
x = 0

window = pygame.display.set_mode((W, H))

CARS=('car1.png', 'car2.png', 'car3.png', 'car4.png')
CARS_SURF=[]
 
for i in range(len(CARS)):
    CARS_SURF.append(pygame.image.load(CARS[i]).convert())
 
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.speed=(randint(5,7))
        self.image.set_colorkey((0,0,0))
    def update(self):
        if self.rect.y < H + 100:
            self.rect.y += self.speed
        else:
            self.kill
 
cars = pygame.sprite.Group()
Car(randint(25,W-25), 50, CARS_SURF[randint(0,2)], cars)
 
class Player(pygame.sprite.Sprite):
    def __init__(self,x, y,surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.image.set_colorkey((0,0,0))
            
player = Player(W//2, (H//2+H//3),CARS_SURF[-1], cars)
window.blit(player.image, player.rect)
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
        elif i.type == pygame.USEREVENT:      
            Car(randint(25,W-25), -10, CARS_SURF[randint(0,2)],cars)
            Car(randint(25,W-25), -10,  CARS_SURF[randint(0,2)],cars)
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.rect.x += 3
        if player.rect.x > (W - 5):
            player.rect.x = W - 5
    elif keys[pygame.K_LEFT]:
        player.rect.x -= 3
        if player.rect.x < 5:
            player.rect.x = 5
    if pygame.sprite.spritecollide(player, cars, False):
        pygame.quit()
        break
    
    pygame.display.set_caption("Машинки /// Времени прожито: " + str(round(x)))
    x += 1/50
    
    window.fill((125,125,125))
    
    cars.draw(window)

    window.blit(player.image, player.rect)
    
    pygame.time.delay(20)
    
    pygame.display.update()
    cars.update()