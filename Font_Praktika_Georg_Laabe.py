import pygame
 
FPS = 16
clock = pygame.time.Clock()

pygame.init()

width = 600
height = 600

window = pygame.display.set_mode((width, height))

t1 = pygame.font.SysFont('arial', 36)
text1 = t1.render('ПЕРЕСЕЧЕНИЕ!!!', 1, (25, 25, 250))

rect1 = pygame.Rect((20, 20, 80, 80))
surf1 = pygame.Surface((80,80))
surf1.fill((255, 25, 25)) 
rect2 = pygame.Rect((225, 225, 150, 150))
surf2 = pygame.Surface((150,150))
surf2.fill((25, 150, 25)) 

window.blit(surf1, rect1)
window.blit(surf2, rect2)

while True:
    
    window.fill((0, 210, 230))
    
    window.blit(surf2, rect2)
    window.blit(surf1, rect1)
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            a,b = pos
            rect1 = pygame.Rect((a-40, b-40, 80, 80))
        
    if rect2.contains(rect1) == 1:
        window.blit(text1, rect1)
             

    pygame.display.set_caption("PyGame Font")
        
    clock.tick(FPS)
    
    pygame.display.update()