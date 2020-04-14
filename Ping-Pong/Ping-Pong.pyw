import pygame
import sys
 
pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND = (100, 150, 250)

x1 = 485
y1 = 250
x2 = 0
y2 = 250

xb = 500
yb = 300

ball_speed = 3

pygame.font.SysFont('arial', 36)

music = pygame.mixer.Sound('lancerfight_tobyfox.ogg')

music.set_volume(0.2)
music.play(-1)

dbo = 0 
dbv = 0 

score1 = 0
score2 = 0

score = pygame.font.Font(None, 36)
score_table = score.render(str('Blue: ' + str(score1) + " | Red: " + str(score2)), 1, (0, 0, 0))

clock = pygame.time.Clock()

game = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Ping-Pong")


def ball():
	global xb, yb
	pygame.draw.ellipse(game, GREEN, (xb, yb, 18, 18))
 
def platform1(y):
	pygame.draw.rect(game, RED, (x1, y, 15, 60))
 
def platform2(y):
	pygame.draw.rect(game, BLUE, (x2, y, 15, 60))
 
def move_ball(x,y):
	global xb, yb, dbo, dbv, ball_speed
	if dbo == 0:
		xb -= ball_speed
	if dbv == 0:
		yb += ball_speed
		if yb > 490:
			dbv = 1
	if dbv:
		yb -= ball_speed
		if yb < ball_speed:
			dbv = 0
	if dbo:
		xb += ball_speed
	
def collision():
	global x1, y1
	global x2, y2 
	global xb, yb
	global x, y
	global dbo
	global score1, score2
	
	if dbo:
		if xb > 476:
			if yb >= y1 and yb < y1 + 60:
				dbo = 0		
			else:
				xb, yb = 10, 50
				pygame.display.update()
				pygame.time.delay(500)
				score1 += 1
				pygame.display.set_caption("Ping-Pong")
	else:
		if xb < 16:
			if yb >= y2 and  yb < y2 + 60:
				dbo = 1
			else:
				xb, yb = 480, 50
				pygame.display.update()
				pygame.time.delay(500)
				score2 += 1
				pygame.display.set_caption("Ping-Pong")
def move1():
	global y1
	if y1 <= 450:
		if keys[pygame.K_DOWN]:
			y1 += 12
	if y1 > 0:
		if keys[pygame.K_UP]:
			y1 -= 12 
            
def move2():
	global y2
	if y2 <= 450:
		if keys[pygame.K_s]:
			y2 += 9
	if y2 > 0:
		if keys[pygame.K_w]:
			y2 -= 9
 
pygame.mouse.set_visible(False)
loop = 1

while loop:
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0
	move1()
	move2()
	move_ball(xb, yb)
	ball()
	platform1(y1)
	platform2(y2)
	collision()
	pygame.display.update()
	clock.tick(60)
	game.fill(BACKGROUND)
	score_table = score.render(str('Blue: ' + str(score1) + " | Red: " + str(score2)), 1, (0, 0, 0))
	game.blit(score_table, (305, 12))
    
pygame.quit()
sys.exit()