#1
string = input("Введите символы: ")
print("Третий символ этой строки - ", string[2])
print("Предпоследний символ это строки - ", string[-2])
print("Первые 5 символов этой строки - ", string[:5])
print("Вся строка, кроме последних 2 символов - ",string[:-2])
print("Все символы с четными индексами - ",string[::2])
print("Все символы с нечетными индексами - ",string[1::2])
print("Все символы в обратном порядке - ",string[::-1])
print("Все символы через один в обратном порядке - ",string[::-2])
print("Длина строки - ",len(string))  

#2
string = input("Введите слова, разделяя их пробелами:")
print(string.count(' ', 0,len(string))+1)

#3
string = input("Введите строку: ")
string_new = (string[int(len(string)/2+1)::1]) + (string[:-int(len(string)/2)]) 
print(string_new)

#4
string = input("Введите 2 слова: ")
string_new = string[string.find(" ",0,len(string))+1:] + " " + string[:string.find(" ",0,len(string))]
print(string_new)

#5
string = input("Введите строку: ")
f_count1 = string.find("f")
f_count2 = string.rfind("f")
if f_count1 == -1 and f_count2 == -1:
    print("")
elif f_count1 == f_count2:
    print(f_count1)
else:
    print(f_count1," ",f_count2)
    
#6
string = input("Введите строку: ")
f_count1 = string.find("f")
string_doll = string[string.find("f")+1:]
f_count2 = int(string.find("f")) + int(string_doll.find("f")) + 1
if f_count1 == f_count2:
    print("-1")
elif f_count2 == -1 and f_count2 == -1:
    print("-2")
else:
    print(f_count2)
    
#7
string = input("Введите строку: ")
print(string[:string.find("h")] + string[string.rfind("h")+1:]) 

#8
string = input("Введите строку: ")
print(string[0:string.find('h')] + string[string.rfind('h'):string.find('h')-1:-1] + string[string.rfind('h')+1:len(string)])

#9
string = input("Введите строку: ")
print(string.replace("1","one"))

#10
string = input("Введите строку: ")
print(string.replace("@",""))

#11
string = input("Введите строку: ")
x = string[string.find('h')+1:string.rfind('h')]
x = x.replace('h','H')
print(string[0:string.find('h')+1] + x + string[string.rfind('h'):len(string)])

#12
string = input("Введите строку: ")
string_new = ''
for x in range(len(string)):
    if x%3 != 0:
        string_new = string_new + string[x]
print(string[0]+string_new)