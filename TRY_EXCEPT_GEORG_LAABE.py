#Примеры ошибок и обработки исключений

#1
x = int(input("Введите делитель: ")) # Задаем значение x
try: # Проверяем на ошибку
    y = 1 / x # Делим любое число на заданное значение
    print(); print("Отлично!\nОтвет:",y) # Выводит успешный результат
except ZeroDivisionError: # Если замечена ошибка...
    print(); print("На ноль делить нельзя!") # Выводим причину

#2
x = input("Введите целое число: ") # Задаем значение x
try: # Проверяем на ошибку
    x = int(x) # Проверяем, является ли число целым
    print(); print("Отлично!") # Выводит успешный результат
except ValueError: # Если замечена ошибка...
    print(); print("ValueError! Это не целое число!") # Выводим причину

#3
try: # Проверяем на ошибку
    Georg += 1 # Применяем какое-либо действие к переменной
except NameError: # Если замечена ошибка...
    print(); print("Не найдено переменной с таким именем!") # Выводим причину