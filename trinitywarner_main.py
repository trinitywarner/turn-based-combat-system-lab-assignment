from character import Hero, Enemy

hero = Hero(name="Hero", health=30, damage=10)
enemy = Enemy(name="Enemy", health=45, damage=15)


while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    
    input()
    

