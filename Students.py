global intelligence
intelligence = 0
class student(object):
    print("\nВот и настала пора учиться!")
    def __init__(self,name):
        self.intelligence = 0
        self.name = name
    def study(self):
        print("\n*Студент номер",self.name ,"учится*")
        self.intelligence += 5
    def iq(self):
        print("\nIQ студента номер",self.name," = ",self.intelligence)
    def leave(self):
        print("\nСтуденты ушли из профтеха!")
stud1 = student("1"); stud2 = student("2")
while True:
    answer = input("Учится первый[1] / Учится второй[2] / Тест[3] / Уйти[4]: ")
    if answer == "Учится первый" or answer == "1":
        stud1.study()
    elif answer == "Учится второй" or answer == "2":
        stud2.study()
    elif answer == "Тест" or answer == "3":
        stud1.iq()
        stud2.iq()
    elif answer == "Уйти" or answer == "4":
        stud1.leave()
        break
    else:
        print("\nТакого варианта нет!")
        continue