#Нормальный код

def reverse(string1): 
    return string1[::-1]   
def pali(string1):
    if string1.replace(' ','') == reverse(string1).replace(' ',''):
        print("Это палиндром!")
    else: 
        print("Это не палиндром!")
        
while True:
    string1 = input("Введите фразу: ").lower()
    reverse(string1)
    pali(string1)
    answer = input("Продолжить?[Да(1)/Нет(2)]: ")
    if answer == "Да" or answer == "1": 
        continue
    else: 
        break


#Супер-короткий код

def reverse(string1): return string1[::-1]   
def pali(string1):
    if string1.replace(' ','') == reverse(string1).replace(' ',''): print("Это палиндром!")
    else: print("Это не палиндром!")
while True:
    string1 = input("Введите фразу: ").lower(); reverse(string1);pali(string1); answer = input("Продолжить?[Да(1)/Нет(2)]: ")
    if answer == "Да" or answer == "1": continue
    else: break