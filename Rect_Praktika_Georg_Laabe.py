import pygame
 
FPS = 16
clock = pygame.time.Clock()

pygame.init()

width = 500
height = 500

window = pygame.display.set_mode((width, height))

flash_first = 0
flash_second = 0
flash_all = 1

backward = 0

rect1 = pygame.Rect((0, 0, 250, 250))
surf1 = pygame.Surface((250,250))
surf1.fill((150, 150, 150)) 
rect2 = pygame.Rect((250, 0, 250, 250))
surf2 = pygame.Surface((250,250))
surf2.fill((150, 150, 150)) 
rect3 = pygame.Rect((0, 250, 250, 250))
surf3 = pygame.Surface((250,250))
surf3.fill((150, 150, 150)) 
rect4 = pygame.Rect((250, 250, 250, 250))
surf4 = pygame.Surface((250,250))
surf4.fill((150, 150, 150)) 

window.blit(surf1, rect1)
window.blit(surf2, rect2)
window.blit(surf3, rect3)
window.blit(surf4, rect4)

pygame.display.update()


while True:
    
    window.fill((0, 210, 230))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_1:
                flash_first = 1
                flash_second = 0
            if i.key == pygame.K_2:
                flash_first = 0
                flash_second = 1
            if i.key == pygame.K_0:
                flash_first = 0
                flash_second = 0
                
    if flash_all == 1 and backward == 0:
        pygame.draw.circle(window, (150,150,150), (250,250), 200)
        backward = 1  
    elif flash_all == 1 and backward == 1:
        pygame.draw.circle(window, (250,250,250), (250,250), 200)    
        backward = 0
    
    if flash_first == 1:
        pygame.display.update(rect1); pygame.display.update(rect4)
    elif flash_second == 1:
        pygame.display.update(rect2); pygame.display.update(rect3)
    else:
        pygame.display.update()
        
    pygame.display.set_caption("Flashing Circle")
        
    clock.tick(FPS)