#Задача 1#
N = int(input('Введите значение: '))
x = 1
while (x ** 2) <= N:
    print(x ** 2)
    x += 1
#Задача 2#
x = 2
y = int(input('Введите значение: '))
while x <= y:
    if (y % x) == 0:
        print(x)
        break
    else:
        x += 1
#Задача 3#      
N = int(input('Введите значение: '))
x = 2
y = 0
while N > x:
    if N > x:
        x *= 2
        y += 1
print(x / 2, ", это 2 в степени ", y)
#Задача 4#
x = int(input("Пробежал в первый день: "))
y = int(input("Пробежал в итоге: "))
day = 1
while x <= y:
    x += (x * 0.1)
    day += 1   
print (day)
#Задача 5#
x = int(input("Введите базовое кол-во денег: "))
p = int(input("Введите процент: "))
y = int(input("Введите итоговое кол-во : "))
year = 0
while x <= y:
    x += x * p / 100
    year += 1    
print (year)  
#Задача 6#
import random
z = 1
y = 0
while z != 0:
        z = random.randrange(0, 20)
        print(z)
        y += 1    
print('Количество сгенерированных чисел :', y - 1)   
#Задача 7#
import random
x = 0
z = 1
while z != 0:
    z = random.randrange(0, 20)
    print(z)
    x += z    
print('Сумма всех элементов последовательности :', x) 
#Задача 8#
import random
y = 0
x = 0
z = 1
mx = 0
while z != 0:
    z = random.randrange(0, 20)
    print(z)
    y += 1
    x += z
    if z >= mx:
        mx = z
    else:
        mx += 0
print('Среднее значение последовательности :', x / y, ', наибольшее значение :', mx)      
#Задача 9#
import random
y = 0
z = 1
mx = 0
q = 0
while z != 0:
    z = random.randrange(0, 20)
    print(z)
    y += 1
    if z >= mx:
        mx = z
        q = y
    else:
        mx += 0
print('Индекс наибольшого значения:', q) 
#Задача 10#
import random
x = 1
len = 0
max = 0
while x != 0:
    x = random.randrange(0, 20)
    print(x)
    len += 1
    if max <= x:
        max = x
    elif len == 20:
        break
    else:
        max += 0
print('Наибольшее значение :', max, ', количество элементов :', len)      
#Табличка умножения#
x = 1
y = 1
while y <= 10:
    print(x, '*', y, "=", x * y)
    x += 1
    if x > 10:
        x = 1
        y += 1
        print("="*15)