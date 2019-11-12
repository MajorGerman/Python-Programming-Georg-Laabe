import os
password = '2365' 
money = 1000
attempts = 3
print("Банкомат имени Георга Лаабе v5.3") 
while attempts > 0:  
    print("") 
    inputed_password = input("Введите пин-код: ")  
    if inputed_password == password:
        print("") 
        print("Добро пожаловать!")
        break       
    else :
        attempts -= 1
        print("") 
        print("У вас осталось попыток:", attempts)   
while attempts > 0:   
    bank_function = input("Введите 1, если вы хотите положить деньги на счет, 2, если хотите снять деньги со счета, 3, если хотите посмотреть баланс или 4, если хотите выйти: ")   
    if bank_function == '1':      
        print("") 
        cash_add = int(input("Сколько денег вы хотите положить? : "))       
        if cash_add >= 0:
            money += cash_add
            print("") 
            print("Деньги внесены! Теперь у вас :", money,"€")    
            print("")                     
        else:
            print("Введите корректное значение")       
    elif bank_function == '2':   
        print("") 
        cash_take = int(input("Сколько денег вы хотите снять? : "))
        if 0 <= cash_take <= money:
            money -= cash_take
            print("") 
            print("Деньги сняты! У вас осталось :", money, "€")
            print("")            
        elif cash_take < 0:
            print("Введите корректное значение!")
            print(" ")       
        else:
            print("Недостаточно средств на счету!")
            print(" ")
    elif bank_function == '3':
        print("") 
        print("Вас счет :", money, "€")
        print("")
    elif bank_function == '4':   
         break   
    else:  
         print("") 
         print("Такой опции нет!")      
if attempts == 0:
    print("")
    print("Ваша карта заблокирована! Вы - грязный хакер!")
    os.system('pause')
else:
    print("")
    print("Спасибо за использование нашего банкомата!")
    print("")
    os.system('pause')