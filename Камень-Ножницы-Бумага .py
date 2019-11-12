import random
x = 1
print("Камень-ножницы-бумага"); print("")
player_name = input("Введите ваше имя: "); print("")
game_count = int(input("Сколько раз вы хотите играть: ")); print("")
comp_choices = ["Камень", "Ножницы", "Бумага"]
wins = loses = draws = 0
while x <= game_count:
    player_choice = input("Выберите оружие (Камень, Ножницы, Бумага): "); print("")
    comp_choice = random.choice(comp_choices)
    if player_choice != "Бумага" and player_choice != "Камень" and player_choice != "Ножницы":
        print("Такого оружия нет!"); print("")
        continue
    print("Компьютер выбрал: ",comp_choice); print("")
    if player_choice == "Камень" and comp_choice == "Бумага":
        print("Победил компьютер"); print("")
        loses += 1
    elif player_choice == "Бумага" and comp_choice == "Ножницы":
        print("Победил компьютер"); print("")
        loses += 1
    elif player_choice == "Камень" and comp_choice == "Ножницы":
        print("Победил ", player_name); print("")
        wins += 1
    elif player_choice == "Бумага" and comp_choice == "Камень":
        print("Победил ", player_name); print("")
        wins += 1
    elif player_choice == "Ножницы" and comp_choice == "Бумага":
        print("Победил ", player_name); print("")
        wins += 1
    elif player_choice == "Ножницы" and comp_choice == "Камень":
        print("Победил компьютер"); print("")
        loses += 1
    else:
        print("Ничья!"); print("")
        draws += 1
    x += 1
    while True:
        if x >= game_count:
                break
                break
        answer = input("Хотите ли вы продолжать?(Да/Нет): ")
        if answer == "Нет":
            x = 99999999999999
            break
            break
        elif answer == "Да":
            break
            continue
        else:
            continue
print("_"*60); print("")
print("Игра окончена! Побед - ",wins, ", поражений - ",loses, ", ничей - ", draws); print("")
input()