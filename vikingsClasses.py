import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    def receiveDamage(self, x):
        self.health = self.health - x

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        Soldier.__init__(self, health, strength)


    def receiveDamage(self, y):
        self.health -= y
        if self.health > 0:
            return f"{self.name} has received {y} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, x):
        self.health -= x
        if self.health > 0:
            return f"A Saxon has received {x} points of damage"
        else:
            return "A Saxon has died in combat"


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = saxon.attack()
        result = viking.receiveDamage(damage)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."



