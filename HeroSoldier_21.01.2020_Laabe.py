import random
goods = []
bads = []
teams = ["goods","bads"]
class Hero():
    command = ""
    level = 0
    def LevelUp(self):
        self.level += 1
class Soldier(Hero):
    command = ""
    def GoToHero(self, hero_any):
        if hero_any == "goods":
            print("Солдат с ид ", self.id, ' идёт за героем "Хороший", с ид', hero_good.id)
        else:
            print("Солдат с ид ", self.id, ' идёт за героем "Плохой", с ид', hero_bad.id)
hero_bad = Hero()
hero_bad.id = 1
hero_good = Hero()
hero_good.id = 2
hero_any = Hero()
for x in range(3,23):
    soldier = Soldier()
    command = random.choice(teams)   
    if command == "goods":
        soldier.command = "good"
        soldier.id = x
        goods.append(soldier)
    else:
        soldier.command = "bads"
        soldier.id = x
        bads.append(soldier)
    if len(goods) > len(bads):
        hero_good.LevelUp()
    else:
        hero_bad.LevelUp()
soldier.GoToHero(command)