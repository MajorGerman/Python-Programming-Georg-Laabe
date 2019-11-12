#1
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
if x < y:
    print("Наименьшее число - ", x)
elif x == y:
    print("Числа равны!")
else:
    print("Наименьшее число - ", y)

#2
sign = 0
x = int(input("Введите число: "))
if x > 0:
    sign = 1
    print(sign)
elif x < 0:
    sign = -1
    print(sign)
else:
    sign = 0
    print(sign)

#3
x1 = int(input("Введите столбец 1 клетки: "))
y1 = int(input("Введите строку 1 клетки: "))
x2 = int(input("Введите столбец 2 клетки: "))
y2 = int(input("Введите строку 2 клетки: "))
place1 = "nocolor"
place2 = "nocolor"
if (x1 == 1 or x1 == 3 or x1 == 5 or x1 == 7) and (y1 == 1 or y1 == 3 or y1 == 5 or y1 == 7):
    place1 = "white"
else:
    place1 = "black"
if (x2 == 1 or x2 == 3 or x2 == 5 or x2 == 7) and (y2 == 1 or y2 == 3 or y2 == 5 or y2 == 7):
    place2 = "white"
else:
    place2 = "black"
if place1 == place2:
    print("");print("YES")
else:
    print("");print("NO")

#4
x = int(input("Введите год :"))
if x % 4 == 0:
    if x % 100 != 0:
        print("YES!")
    elif x % 400 == 0:
        print("YES!")
    else:
        print("NO!")
else:
    print("NO!")
        
#5
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))
if x < y and x < z:
    print("Наименьшее число -",x)
elif y < x and y < z:
    print("Наименьшее число -",y)
else:
    print("Наименьшее число -",z)
    
#6
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))
if x == y == z:
    print(3)
elif x == y or y == z or z == x:
    print(2)
else:
    print(0)
    
#7
x1 = int(input("Введите столбец 1 клетки: "))
y1 = int(input("Введите строку 1 клетки: "))
x2 = int(input("Введите столбец 2 клетки: "))
y2 = int(input("Введите строку 2 клетки: "))
if x1 == x2 or y1 == y2:
    print("");print("YES")
else:
    print("");print("NO")
    
#8
x1 = int(input("Введите столбец 1 клетки: "))
y1 = int(input("Введите строку 1 клетки: "))
x2 = int(input("Введите столбец 2 клетки: "))
y2 = int(input("Введите строку 2 клетки: "))
if x1-1 <= x2 <= x1+1 and y1-1 <= y2 <= y1+1:
    print("");print("YES")
else:
    print("");print("NO")

#9
x1 = int(input("Введите столбец 1 клетки: "))
y1 = int(input("Введите строку 1 клетки: "))
x2 = int(input("Введите столбец 2 клетки: "))
y2 = int(input("Введите строку 2 клетки: "))
if x1-x2 == y1-y2 or x1-x2 == -(y1-y2):
    print("");print("YES")
else:
    print("");print("NO")
    
#10
x1 = int(input("Введите столбец 1 клетки: "))
y1 = int(input("Введите строку 1 клетки: "))
x2 = int(input("Введите столбец 2 клетки: "))
y2 = int(input("Введите строку 2 клетки: "))
if x1 == x2 or y1 == y2 or x1-x2 == y1-y2 or x1-x2 == -(y1-y2):
    print("");print("YES")
else:
    print("");print("NO")
    
#11
x1 = int(input("Введите столбец 1 клетки: "))
y1 = int(input("Введите строку 1 клетки: "))
x2 = int(input("Введите столбец 2 клетки: "))
y2 = int(input("Введите строку 2 клетки: "))
if (x2-x1 == 2 and y2-y1 == 1) or (x2-x1 == -2 and y2-y1 == -1) or (y2-y1 == 2 and x2-x1 == 1) or (y2-y1 == -2 and x2-x1 == -1):
    print("");print("YES")
else:
    print("");print("NO")

#12
n = int(input("Введите длину шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Введите число долек: "))
answer = False
for a in range(1, n):
    c = a * n
    if c == k:
        answer = True
        break
        break
    else:
        for b in range(1, m):
            d = b * m
            if d == k:
                answer = True
                break
                break
                break
            else:
                continue
if answer == True:
    print("YES")
else:
    print("NO")

#Задача про Яшу 
N = int(input("Введите длину бассейна: "))
M = int(input("Введите ширину бассейна: "))
x = int(input("Введите расстояние от длинного бортика: "))
y = int(input("Введите расстояние от короткого бортика: "))
if x<=N//2 and y<=M//2:
    if x<y:
        print("Минимально он должен проплыть: ", x)
    else:
        print("Минимально он должен проплыть: ", y)
elif x>N//2 and y<M//2:
    if (N-x)<y:
        print("Минимально он должен проплыть: ", N-x)
    else:
        print("Минимально он должен проплыть: ", y)
elif x>N//2 and y>M//2:
    if N-x<M-y:
        print("Минимально он должен проплыть: ", N-x)
    else:
        print("Минимально он должен проплыть: ", M-y)
elif x<N//2 and y>M//2:
    if x<M-y:
        print("Минимально он должен проплыть: ", x)
    else:
        print("Минимально он должен проплыть: ", M-y)   
        
#Задача на ставку
import random
wins = 0
print("Ставочник 2019");print("____"*15)
comp_choice = random.randint(1,50)
game_count = int(input("Сколько раз вы хотите играть? : "))
game_played = 0
while game_played < game_count:
    x = int(input("Введите число от 1 до 50: "));print("")
    game_played += 1
    if x == comp_choice:
       print("Ставка сыграла!")
       input("Введите 1, чтобы продолжить или 2, что закончить: ")
       
    else:
        continue
