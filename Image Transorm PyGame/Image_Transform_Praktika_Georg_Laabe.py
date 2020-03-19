import pygame
 
FPS = 60
clock = pygame.time.Clock()

pygame.init()

width = 600
height = 600

window = pygame.display.set_mode((width, height))

car = pygame.image.load("car.png")
car_main = pygame.image.load("car.png")

x = 300
y = 300 
ku = 1

window.blit(car, (x, y))

while True:
    
    window.fill((0, 210, 230))
    
    window.blit(car,  (x, y))
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        car = pygame.transform.rotate(car_main, 90)
        x -= 3.25
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        car = pygame.transform.rotate(car_main, 270)
        x += 3.25
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        car = pygame.transform.rotate(car_main, 0)
        y -= 3.25
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        car = pygame.transform.rotate(car_main, 180)
        y += 3.25

    pygame.display.set_caption("PyGame Image Transform")
        
    clock.tick(FPS)
    
    pygame.display.update()