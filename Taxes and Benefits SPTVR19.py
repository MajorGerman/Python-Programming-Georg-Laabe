money = 0
money_lose = 0

def childcash(children):
    global money
    if children <= 2:
        money += 60 * children
        print("\nВ семье менее трех детей. На каждого приходится 60€, на всех - ", 60 * children,"€")
    else:
        money += 100 * children
        print("\nВ семье более двух детей. На каждого приходится 100€, на всех - ", 100 * children,"€")
       
def cash(a):
    global money
    global money_lose
    a -= cons_cash
    money +=  a - (a * 0.02) - (a * 0.016) - (a * 0.2) + cons_cash
    money_lose += a * 0.02 + a * 0.016 + a * 0.2 
    print("\nВычитаемая накопительная пенсия - ",round((a * 0.02),2),"€","(2%)")
    print("Вычитаемый налог по безработице - ",round((a * 0.016),2),"€","(1.6%)")
    print("Вычитаемый подоходный налог - ",round((a * 0.2),2),"€","(20%)")
    print("Необлогаемая налогом сумма - ",round(cons_cash,2),"€")

while True:
    adult = int(input("Введите кол-во взрослых людей: "))
    if adult <= 1:
        print("Взрослых людей не может быть менее двух!")
        continue
    break

while True:
    children = int(input("Введите кол-во детей: "))
    if children <= 1:
        print("Детей не может быть менее двух!")
        continue
    break

for x in range (1, adult+1):
    a = int(input("Какая брутто-зарплата у взрослого человека:"))
    cons_cash = 500 - 0.55556 * (a - 1200)
    if cons_cash >= 500:
        cons_cash = 500
    if cons_cash <= 0:
        cons_cash = 0
    if (a + cons_cash) < 540:
        print("Слишком маленькая зарплата!")
        continue
    cash(a)
    
childcash(children)

print("\n////////////////////////")
print("\nДоход семьи за месяц (Нетто-зарплаты и детские пособия): ", round(money,2),"€")
print("Доход семьи за год: ", round((money * 12),2),"€; Государство получило за год: ",round((money_lose * 12),2),"€")