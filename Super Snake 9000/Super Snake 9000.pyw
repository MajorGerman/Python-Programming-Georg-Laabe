import pygame
from random import randrange
pygame.init() # Инициализируем Пайгейм
white = (255, 255, 255)  # Предсоздаем нужные цвета
magenta = (185, 75, 195)
red = (255, 25, 25)
green = (0, 255, 0)
blue = (76, 151, 243)
yellow = (230,230,10)
width = 800; height = 800 # Ставим размеры
game = pygame.display.set_mode((width, height)) # Создаем окно
pygame.display.set_caption('Super Snake 9000') # Ставим заголовок
clock = pygame.time.Clock()
snake_block = 25  # Делаем размер змейки
snake_speed = 9   # Делаем скорость змейки
font_style = pygame.font.SysFont("arial", 36)   # Создаем шрифты
score_font = pygame.font.SysFont("arial", 28)
def Your_score(score):   # Функция счета
    value = score_font.render("Счет: " + str(score), True, yellow)
    game.blit(value, [0, 0])
def our_snake(snake_block, snake_list):   # Змейки
    for x in snake_list:
        pygame.draw.rect(game, magenta, [x[0], x[1], snake_block, snake_block])
def message(msg, color):                  # Функция сообщения
    mesg = font_style.render(msg, True, color)
    game.blit(mesg, [width / 5 + 60, height / 3 + 60])  
def gameLoop():                           # Функция игры
    game_over = False
    game_close = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1 
    food_x = round(randrange(0, width - snake_block) /25) * 25   # Еда
    food_y = round(randrange(0, height - snake_block) /25) * 25
    while not game_over:       # Основной цикл
        while game_close == True:  
            game.fill(blue)
            message("Нажмите C для перезапуска!", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():    
                if event.type == pygame.KEYDOWN:  # События клавиатуры 1
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      # Выход из игры
                pygame.quit()  
                game_over = True
                exit()  
            if event.type == pygame.KEYDOWN:   # События клавиатуры 2
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game.fill(blue)
        pygame.draw.rect(game, green, [food_x, food_y, snake_block, snake_block])  # Рисуется еда
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 <= food_x+15 and x1 >= food_x-15 and y1 <= food_y+15 and y1 >= food_y-15:  # Съедается еда
            food_x = round(randrange(0 + snake_block, width - snake_block)/25) * 25
            food_y = round(randrange(0 + snake_block, width - snake_block)/25) * 25
            Length_of_snake += 1
        clock.tick(snake_speed)    # Тик
    pygame.quit()
    quit()
gameLoop()