import pygame
import time
import random
import os 

width = 660
height = 660

clock = pygame.time.Clock()

count1 = 0
count2 = 0
count3 = 0

def main(count1,count2, count3):
    
    pygame.init()
    game = pygame.display.set_mode((width, height))
    pygame.display.update()
    
    cage1 = ""
    cage2 = ""
    cage3 = ""
    cage4 = ""
    cage5 = ""
    cage6 = ""
    cage7 = ""
    cage8 = ""
    cage9 = ""
    
    your_turn = True
    
    crosspath = os.getcwd() + "\cross.png"
    circlepath = os.getcwd() + "\circle.png"
    
    cross = pygame.image.load(crosspath) 
    cross = pygame.transform.scale(cross, (int(width/3)-10,int(height/3)-10))
    circle = pygame.image.load(circlepath) 
    circle = pygame.transform.scale(circle, (int(width/3)-10,int(height/3)-10))
    
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and your_turn == True:
                    a,b = i.pos
                    if a < int(width/3) and b < int(height/3) and cage1 == "":                                         #1
                        time.sleep(0.06)
                        game.blit(cross, (10,10))
                        your_turn = False
                        cage1 = "cross"
                    elif int(width/3) < a < int(width/3)*2 and b < int(height/3) and cage2 == "":                     #2
                        time.sleep(0.06)
                        game.blit(cross, (width/3,10))
                        your_turn = False
                        cage2 = "cross"
                    elif a > int(width/3)*2 and b < int(height/3) and cage3 == "":                                     #3
                        time.sleep(0.06)
                        game.blit(cross, ((width/3)*2,10))
                        your_turn = False
                        cage3 = "cross"
                    elif a < int(width/3) and int(height/3) < b < int(height/3)*2 and cage4 == "":                     #4
                        time.sleep(0.06)
                        game.blit(cross, (10,height/3))
                        your_turn = False
                        cage4 = "cross"
                    elif int(width/3) < a < int(width/3)*2 and int(height/3) < b < int(height/3)*2 and cage5 == "":   #5
                        time.sleep(0.06)
                        game.blit(cross, (width/3,height/3))
                        your_turn = False
                        cage5 = "cross"                    
                    elif a > int(width/3)*2 and int(height/3) < b < int(height/3)*2 and cage6 == "":                   #6
                        time.sleep(0.06)
                        game.blit(cross, ((width/3)*2,height/3))
                        your_turn = False
                        cage6 = "cross"
                    elif a < int(width/3) and b > int(height/3)*2 and cage7 == "":                                     #7
                        time.sleep(0.06)
                        game.blit(cross, (10,(height/3)*2))
                        your_turn = False
                        cage7 = "cross"
                    elif int(width/3) < a < int(width/3)*2 and b > int(height/3)*2 and cage8 == "":                   #8
                        time.sleep(0.06)
                        game.blit(cross, (width/3,(height/3)*2))
                        your_turn = False
                        cage8 = "cross"
                    elif a > int(width/3)*2 and b > int(height/3)*2 and cage9 == "":                                   #9
                        time.sleep(0.06)
                        game.blit(cross, ((width/3)*2,(height/3)*2))
                        your_turn = False
                        cage9 = "cross"
                else:
                    continue
                
            if your_turn == False:           
                if cage1 == "circle" and cage5 == "circle" and cage9 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)*2))
                    cage9 = "circle"
                    your_turn = True
                    continue
                if cage3 == "circle" and cage5 == "circle" and cage7 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)*2))
                    cage7 = "circle"
                    your_turn = True
                    continue
                if cage9 == "circle" and cage5 == "circle" and cage1 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,10))
                    cage1 = "circle"
                    your_turn = True
                    continue
                if cage7 == "circle" and cage5 == "circle" and cage3 == "":
                    time.sleep(0.06)
                    game.blit(circle, (((width/3)*2),10))
                    cage3 = "circle"
                    your_turn = True
                    continue
                if cage4 == "circle" and cage6 == "circle" and cage5 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),(height/3)))
                    cage5 = "circle"
                    your_turn = True
                    continue
                if cage2 == "circle" and cage8 == "circle" and cage5 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),(height/3)))
                    cage5 = "circle"
                    your_turn = True
                    continue
                if cage2 == "circle" and cage5 == "circle" and cage8 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),(height/3)*2))
                    cage8 = "circle"
                    your_turn = True
                    continue
                if cage4 == "circle" and cage5 == "circle" and cage6 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)))
                    cage6 = "circle"
                    your_turn = True
                    continue
                if cage8 == "circle" and cage5 == "circle" and cage2 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),10))
                    cage2 = "circle"
                    your_turn = True
                    continue
                if cage6 == "circle" and cage5 == "circle" and cage4 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)))
                    cage4 = "circle"
                    your_turn = True
                    continue
                if cage1 == "circle" and cage3 == "circle" and cage2 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),10))
                    cage2 = "circle"
                    your_turn = True
                    continue
                if cage1 == "circle" and cage7 == "circle" and cage4 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)))
                    cage4 = "circle"
                    your_turn = True
                    continue
                if cage3 == "circle" and cage9 == "circle" and cage6 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)))
                    cage6 = "circle"
                    your_turn = True
                    continue
                if cage7 == "circle" and cage9 == "circle" and cage8 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3,(height/3)*2)))
                    cage8 = "circle"
                    your_turn = True
                    continue
                if cage1 == "circle" and cage2 == "circle" and cage3 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,10))
                    cage3 = "circle"
                    your_turn = True
                    continue
                if cage3 == "circle" and cage2 == "circle" and cage1 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,10))
                    cage1 = "circle"
                    your_turn = True
                    continue
                if cage1 == "circle" and cage4 == "circle" and cage7 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)*2))
                    cage7 = "circle"
                    your_turn = True
                    continue
                if cage7 == "circle" and cage4 == "circle" and cage1 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,10))
                    cage1 = "circle"
                    your_turn = True
                    continue
                if cage3 == "circle" and cage6 == "circle" and cage9 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)*2))
                    cage9 = "circle"
                    your_turn = True
                    continue
                if cage9 == "circle" and cage6 == "circle" and cage3 == "":
                    time.sleep(0.06)
                    game.blit(circle, (width/3,10))
                    cage3 = "circle"
                    your_turn = True
                    continue
                if cage7 == "circle" and cage8 == "circle" and cage9 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)*2))
                    cage9 = "circle"
                    your_turn = True
                    continue
                if cage9 == "circle" and cage8 == "circle" and cage7 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)*2))
                    cage7 = "circle"
                    your_turn = True
                    continue     
                
                if cage1 == "cross" and cage5 == "cross" and cage9 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)*2))
                    cage9 = "circle"
                    your_turn = True
                    continue
                if cage3 == "cross" and cage5 == "cross" and cage7 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)*2))
                    cage7 = "circle"
                    your_turn = True
                    continue
                if cage9 == "cross" and cage5 == "cross" and cage1 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,10))
                    cage1 = "circle"
                    your_turn = True
                    continue
                if cage7 == "cross" and cage5 == "cross" and cage3 == "":
                    time.sleep(0.06)
                    game.blit(circle, (((width/3)*2),10))
                    cage3 = "circle"
                    your_turn = True
                    continue
                if cage4 == "cross" and cage6 == "cross" and cage5 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),(height/3)))
                    cage5 = "circle"
                    your_turn = True
                    continue
                if cage2 == "cross" and cage8 == "cross" and cage5 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),(height/3)))
                    cage5 = "circle"
                    your_turn = True
                    continue
                if cage2 == "cross" and cage5 == "cross" and cage8 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),(height/3)*2))
                    cage8 = "circle"
                    your_turn = True
                    continue
                if cage4 == "cross" and cage5 == "cross" and cage6 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)))
                    cage6 = "circle"
                    your_turn = True
                    continue
                if cage8 == "cross" and cage5 == "cross" and cage2 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),10))
                    cage2 = "circle"
                    your_turn = True
                    continue
                if cage6 == "cross" and cage5 == "cross" and cage4 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)))
                    cage4 = "circle"
                    your_turn = True
                    continue
                if cage1 == "cross" and cage3 == "cross" and cage2 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3),10))
                    cage2 = "circle"
                    your_turn = True
                    continue
                if cage1 == "cross" and cage7 == "cross" and cage4 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)))
                    cage4 = "circle"
                    your_turn = True
                    continue
                if cage3 == "cross" and cage9 == "cross" and cage6 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)))
                    cage6 = "circle"
                    your_turn = True
                    continue
                if cage7 == "cross" and cage9 == "cross" and cage8 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3,(height/3)*2)))
                    cage8 = "circle"
                    your_turn = True
                    continue
                if cage1 == "cross" and cage2 == "cross" and cage3 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,10))
                    cage3 = "circle"
                    your_turn = True
                    continue
                if cage3 == "cross" and cage2 == "cross" and cage1 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,10))
                    cage1 = "circle"
                    your_turn = True
                    continue
                if cage1 == "cross" and cage4 == "cross" and cage7 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(width/3)*2))
                    cage7 = "circle"
                    your_turn = True
                    continue
                if cage7 == "cross" and cage4 == "cross" and cage1 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,10))
                    cage1 = "circle"
                    your_turn = True
                    continue
                if cage3 == "cross" and cage6 == "cross" and cage9 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)*2))
                    cage9 = "circle"
                    your_turn = True
                    continue
                if cage9 == "cross" and cage6 == "cross" and cage3 == "":
                    time.sleep(0.06)
                    game.blit(circle, (width/3,10))
                    cage3 = "circle"
                    your_turn = True
                    continue
                if cage7 == "cross" and cage8 == "cross" and cage9 == "":
                    time.sleep(0.06)
                    game.blit(circle, ((width/3)*2,(height/3)*2))
                    cage9 = "circle"
                    your_turn = True
                    continue
                if cage9 == "cross" and cage8 == "cross" and cage7 == "":
                    time.sleep(0.06)
                    game.blit(circle, (10,(height/3)*2))
                    cage7 = "circle"
                    your_turn = True
                    continue
                
                a = random.randint(1,10)
                
                if a == 1 and cage1 == "":
                    if cage1 != "":
                        a += 1 
                    else:
                        your_turn = True 
                        time.sleep(0.06)
                        game.blit(circle, (10,10))
                        cage1 = "circle"
                        your_turn = True
                elif a == 2 and cage2 == "":
                    if cage1 != "":
                        a += 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, (width/3,10))
                        cage2 = "circle"
                        your_turn = True
                elif a == 3 and cage3 == "":
                    if cage3 != "":
                        a += 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, ((width/3)*2,10))
                        cage3 = "circle"
                        your_turn = True
                elif a == 4 and cage4 == "":
                    if cage4 != "":
                        a += 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, (10,height/3))
                        cage4 = "circle"
                        your_turn = True
                elif a == 5 and cage5 == "":
                    if cage5 != "":
                        a += 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, (width/3,height/3))
                        cage5 = "circle"
                        your_turn = True
                elif a == 6 and cage6 == "":
                    if cage6 != "":
                        a += 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, ((width/3)*2,height/3))
                        cage6 = "circle"
                        your_turn = True
                elif a == 7 and cage7 == "":
                    if cage7 != "":
                        a += 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, (10,(height/3)*2))
                        cage7 = "circle"
                        your_turn = True
                elif a == 8 and cage8 == "":
                    if cage8 != "":
                        a += 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, (width/3,(height/3)*2))
                        cage8 = "circle"
                        your_turn = True
                elif a == 9 and cage9 == "":
                    if cage9 != "":
                        a = 1
                    else:
                        time.sleep(0.06)
                        game.blit(circle, ((width/3)*2,(height/3)*2))
                        cage9 = "circle"
                        your_turn = True    
                    
        clock.tick(60)

        pygame.display.set_caption("Крестики-Нолики /// Побед: " + str(count1) + " / Поражений: " + str(count2) + " / Ничей: " + str(count3))
        
        pygame.draw.line(game, (255,255,255), [10, 10], [10, height-10], 4)
        pygame.draw.line(game, (255,255,255), [10, 10], [width-10, 10], 4)
        pygame.draw.line(game, (255,255,255), [width-10, 10], [width-10, height-10], 4)
        pygame.draw.line(game, (255,255,255), [10, height-10], [width-10, height-10], 4)
        
        pygame.draw.line(game, (255,255,255), [int(width/3), 10], [int(width/3), height-10], 4)
        pygame.draw.line(game, (255,255,255), [(int(width/3))*2, 10], [(int(width/3))*2, height-10], 4)
        pygame.draw.line(game, (255,255,255), [10, int(height/3)], [width-10, int(height/3)], 4)
        pygame.draw.line(game, (255,255,255), [10, int(height/3)*2], [width-10, int(height/3)*2], 4)
        
        pygame.display.update()
        
        if cage1 == "cross" and cage2 == "cross" and cage3 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
        if cage4 == "cross" and cage5 == "cross" and cage6 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
        if cage7 == "cross" and cage8 == "cross" and cage9 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
        if cage1 == "cross" and cage4 == "cross" and cage7 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
        if cage2 == "cross" and cage5 == "cross" and cage8 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
        if cage3 == "cross" and cage6 == "cross" and cage9 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
        if cage1 == "cross" and cage5 == "cross" and cage9 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
        if cage3 == "cross" and cage5 == "cross" and cage7 == "cross":
            time.sleep(0.35)
            count1 += 1
            main(count1,count2, count3)
            
        if cage1 == "circle" and cage2 == "circle" and cage3 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
        if cage4 == "circle" and cage5 == "circle" and cage6 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
        if cage7 == "circle" and cage8 == "circle" and cage9 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
        if cage1 == "circle" and cage4 == "circle" and cage7 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
        if cage2 == "circle" and cage5 == "circle" and cage8 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
        if cage3 == "circle" and cage6 == "circle" and cage9 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
        if cage1 == "circle" and cage5 == "circle" and cage9 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
        if cage3 == "circle" and cage5 == "circle" and cage7 == "circle":
            time.sleep(0.35)
            count2 += 1
            main(count1,count2, count3)
            
        if cage1 != "" and cage2 != "" and cage3 != "" and cage4 != "" and cage5 != "" and cage6 != ""and cage7 != "" and cage8 != "" and cage9 != "":
            time.sleep(0.35)
            count3 += 1
            main(count1,count2, count3) 
        
    quit()
    
main(count1,count2, count3)