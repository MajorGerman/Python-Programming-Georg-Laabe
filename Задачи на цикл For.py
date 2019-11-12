#1

# Примеры применения циклов FOR(1)

for linn in 'Narva', 'Toila', 'Oru':
    print(linn)
print()

x = 1
for linn in 'Narva', 'Toila', 'Oru':
    print(x, linn)
    x += 1
print()

for i in 1, 2, 3, 'üks', 'kaks', 'kolm':
    print(i)
print()

sum = 0
for i in 10, 12, 13, 20, 5, 8:
    sum += i
    print(i)
print("Sum of numbers = ", sum)
print("_"*20)

#2

# Примеры применения циклов FOR(2)
# Range - интервал

a="Tere tulemast"
for i in range (5):
    print(a)
print("")

a="Tere"
for i in range(5):
    print(i, a)
    
a="Привет!"
for i in range (1,5):
    print(i, a)
print("")

a="Добро пожаловать!"
for i in range(1,6):
    print (i,a)
print("")

for k in range (2,5):
    print("k = ", k)
    
for i in range(1, 100,10):
    print(i)
print("")

# Эквивалентно

print("="*25)
for i in range(0,21,2):
    print(i)
    
print("="*25)
for i in range(21):
    if i % 2 == 0:
        print(i)
        
print()

#3

# Циклы и печать
# Настройка функции print()

print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=", ", end=". ")
print(4, 5, 6, sep=", ", end=". ")
print()
print(1, 2, 3, sep="", end=" -- ")
print(4, 5, 6, sep=" * ", end=".")
print()
print("-"*20)

# Применение циклов
a = 3
for i in range(5):
    print (a, " ", end="")
print("")

a = 10
for i in range(5):
    print(a, " ", end="")

for i in range (10):
    print("-", i, end="")
print()
print("-"*20)

print ('Sum of numbers from 1 to 5')
print('Number Sum')
sum = 0
n = 5
for i in range(1, n+1):
    sum += i
    print(i, '\t', sum) #Сумма с накоплением
print("-"*20)
print('Final Sum = ', sum)

#4

# Найти максимальное значение последовательности
# и количество её элементов

# В программе генерируется случайным образом
# последовательность целых неотрицательных чисел,
# каждое число выводится на экран, пока
# не сгенерировано число 0 или количество
# сгенерированных чисел больше 20. В этом случае
# программа должна закончить свою работу,
# вывести значение наибольшего элемента
# последовательности и количество элементов.

'''---- 1 ----'''
import random
max = 0
arv = random.randint(0,50)
print('Последовательность случайных чисел:')

while arv != 0:
    print(arv)
    if max < arv:
        max = arv
    arv = random.randint(0,50)
print('Максимальный элемент последовательности: ', max)

'''---- 2 ----'''
import random
count = 0
max = 0
arv = random.randint(0,50)
print('Полсдеовательность случайных чисел:')

while count <= 20:
    count += 1
    if arv == 0: # Выход из цикла
        break
    else:
        if max < arv:
            max = arv
        print(arv)
        arv = random.randint(0,50)
print('Максимальный элемент последовательности: ', max)
print('Количество элементов в последовательности :', count-1)