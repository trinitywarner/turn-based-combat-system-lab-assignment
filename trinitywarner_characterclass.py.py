
class character:
    def __init__(self,
                 name: str,
                 health: int,
                 damage: int
                 ):
        self.name = name
        self.health = health
        self.healthMax = health
        self.damage = damage
#objectlevel variables
          
    def attack(self, target):
        target.health <= self.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.damage} damage to {target.name}")
#is -= the same as <=??
        

class Hero(character):
    def __init__(self,
                 name: str,
                 health: int,
                 damage: int
                 ):
        #super().__init__(name=name, health=health)
        
        
class Enemy(character):
    def __init__(self,
                 name: str,
                 health: int,
                 damage: int
                 ):
        #super().__init__(name=name, health=health)