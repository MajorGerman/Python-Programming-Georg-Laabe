##### OOP_03 #####

### 1 ###
class Dog():
    age = 0
    name = ""
    weight = 0
Laika = Dog()
Laika.age = 4
Laika.name = "Лайка"
Laika.weight = 20

### 2 ###
class Person():
    name = ""
    cellPhone = ""
    email = ""
John = Person()
John.name = "John"
John.cellPhone = "37258317253"
John.email = "john1408@gmail.com"
Mary = Person()
Mary.name = "Mary"
Mary.cellPhone = "37256302440"
Mary.email = "marybest33@gmail.com"

### 3 ###
class Bird():
    name = ""
    color = ""
    breed = ""
myBird = Bird()
myBird.color = "green"
myBird.name = "Sunny"
myBird.breed = "Sun Conure"

### 4 ###
class Player():
    name = ""
    x_position = 0
    y_position = 0
    health = 0
    strenght = 0
player1 = Player()
player1.name = "Dylan"
x_position = 4
y_position = 4
health = 100
strenght = 15

### 5 ###
class Person:
    name = ""
    money = 0

nancy = Person()
name = "Nance"
money = 100

# Программист забыл обратиться к экземпляру
# Также после названия класса следует ставить скобки

class Person():
    name = ""
    money = 0

nancy = Person()
nancy.name = "Nance"
nancy.money = 100

### 6 ###
class Person:
    name = ""
    money = 0
    
bob = Person()
print (bob.name, "has",money, "dollars.")

# Программист забыл обратиться  к экземпляру
# Также после названия класса следует ставить скобки

class Person():
    name = ""
    money = 0
    
bob = Person()
print(bob.name, "has",bob.money, "dollars.")

### 7 ###

# Программист не задал имя, поэтому принтуется базовое нулевое значение

class Person():
    name = ""
    money = 0
    
bob = Person()
bob.name = "Bob"
print(bob.name, "has",bob.money, "dollars.")

##### OOP_04 #####

### 1 ###
class Cat():
    name = ""
    color = ""
    weight = 0
    def meow(self):
        print("MEEEOWWW")
Peach = Cat()
Peach.name = "Peach"
Peach.weight = 8
Peach.color = "Orange-White"
Peach.meow()

### 2 ###
class Aadress():
    name = ""
    country = ""
    location = ""
    def data(self):
        print("Name: ", self.name)
        print("Country: ", self.country)
        print("Location: ", self.location)

tech = Aadress()
tech.name = "IVKHK"
tech.country = "Estonia"
tech.location = "Tallinna maantee 13"


### 3 ###
class Monster():
    name = ""
    health = 100
    def decreaseHealth(self, amount):
        self.health -= amount
        if self.health < 0:
            print("* Монстр умер *")
nikita = Monster()

##### ПРАКТИЧЕСКАЯ РАБОТА (КЛАСС "ВОИН") #####
import random
class Warrior():
    health = 0
    def getDamage(self):
        self.health -= 20
pers_1 = Warrior()
pers_1.health = 100
pers_2 = Warrior()
pers_2.health = 100
while pers_1.health > 0 and pers_2.health > 0:
    choice = random.randint(1,2)
    if choice == 1:
        pers_2.getDamage()
        print("\nВоин 1 ударил воина 2")
        print("Здоровье воина 1: ",pers_1.health)
        print("Здоровье воина 2: ",pers_2.health)
    else:
        pers_1.getDamage()
        print("\nВоин 2 ударил воина 1")
        print("Здоровье воина 1: ",pers_1.health)
        print("Здоровье воина 2: ",pers_2.health)
if pers_1.health <= 0:
    print("\nПобедил воин 2!")
else :
    print("\nПобедил воин 1!")