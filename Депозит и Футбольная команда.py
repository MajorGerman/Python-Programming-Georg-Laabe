#Набор в футбольную команду
print("Программа набора в футбольную команду")
while True:
    sex = input("Выберите пол (М/Ж) : ")
    if sex == "Ж":
        print("Вы нам не подходите!");break
    elif sex == "М":
        age = int(input("Введите ваш возраст: "))
        if age in range (16,19):
            print("Вы нам подходите!");break
        else:
            print("Вы нам не подходите!");break
    else:
        print("Выберите корректный пол!");continue

#Депозитный банк
print("Депозитный банк")
money = int(input("Введите сумму депозита : "))
percent = int(input("Введите процент: "))
years = int(input("Введите количество лет: "))
benefit = 0
print("")
for x in range(1,years+1):
    print("#", x, "Начальная сумма - ", "{0:2d}".format(int(round(money,2))), ", интресс - ", "{0:2d}".format(int(round(money * (percent / 100),2))),", итоговая сумма - ", "{0:2d}".format(int(round(money + money * (percent / 100),2))))
    benefit += money * (percent / 100); money += money * (percent / 100)
print("");print("Итоговая сумма составила - ",round(money, 2),", а прибыль составила - ", round(benefit,2))

