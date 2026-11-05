import random

class Hero:
    def __init__(self, name):
        self.name = name
        self._health = 100
        self._level = 0

    def __str__(self):
        return f"Hero Name: {self.name}\nHero HP: {self._health}\nHero Level: {self._level}"
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, health):
        if health < 0:
            self._health = 0
        elif health > 100:
            self._health = 100
        else:
            self._health = health

    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self._health = 100
        print(f"{self.name} is leveling up to {self._level}")

class Monster:
    def __init__(self, name):
        self.name = name
        self._health = 75
        self._level = 1

    def __str__(self):
        return f"Monster Name: {self.name}\nMonster HP: {self._health}\nMonster Level: {self._level}"

    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, health):
        if health < 0:
            self._health = 0
        elif health > 100:
            self._health = 100
        else:
            self._health = health

    def level(self):
        return self._level

    def damage(self):
        return random.randint(5,10)
    
    
def main():
    character_names = ["Odysseus", "Percy", "Grover"]  # These are the character names a user can choose from
    hero = ""
    mon = Monster("Gargoyle")
    
    weapons = {                     # These are the weapon names and damage that a user can choose from
    "Baseball Bat": 15,
    "Spiky Club": 20,
    "Excalibur": 50
    }

    chosen_weapon = ""


    name = input("What is your name? ").strip().title()
    print(f"Hello {name}! Welcome to John's RPG Game. ")

    print("Hero Options: ")

    for index, character in enumerate(character_names):
        print(f"{index+1}: {character}")

    while hero == "":
        try:
            character_choose = int(input("Which Hero do you want? (numbers only): "))   # When a user chooses a specific number they 
            if character_choose == 1:                                                   # can will initiize the hero classes
                print(f"You chose '{character_names[0]}'!")
                hero = Hero(f"{character_names[0]}")
            elif character_choose == 2:
                print(f"You chose {character_names[1]}!")
                hero = Hero(f"{character_names[1]}")
            elif character_choose == 3:
                print(f"You chose {character_names[2]}!")
                hero = Hero(f"{character_names[2]}")
            else:
                print("Please enter numbers (1-3)")
        except ValueError:
            print("Please enter a number! ")


    print(f"These are {hero.name}'s current stats:\n{hero}\n")

    print("Weapon options: ")
    for index, (key, value) in enumerate(weapons.items()):
        print(f"{index+1}: {key} | Damage: {value}")
    while chosen_weapon == "":
        try:
            weapon_choose = int(input("Which weapon do you want? (numbers only): "))
            if weapon_choose == 1:
                print(f"You chose '{list(weapons)[0]}'")
                chosen_weapon = list(weapons)[0]
            elif weapon_choose == 2:
                print(f"You chose '{list(weapons)[1]}'")
                chosen_weapon = list(weapons)[1]
            elif weapon_choose == 3:
                print(f"You chose '{list(weapons)[2]}'")
                chosen_weapon = list(weapons)[2]
            else:
                print("Please enter numbers (1-3)")
        except ValueError:
            print("Please enter a number! ")

    hero_damage = weapons[chosen_weapon]

    print(f"\nTime to Fight!!!\n")
    print(f"{name}, {hero.name} is going to fight {mon.name}!")

    while hero._health >= 0 and mon._health >= 0:
        print(f"{hero.name} did {hero_damage} damage to {mon.name}!")
        mon.health -= hero_damage
        print(f"Monster: {mon.name} is currently at {mon._health} HP")
        if (hero._health <= 0):
            print(f"Game over: {hero.name} has died! ")
            return
        if (mon._health <= 0):
            print(f"Victory!!! {mon.name} has been slain!!!")
            print(f"")
            return
        dam_hit = mon.damage()
        print(f"{mon.name} did {dam_hit} damage to {hero.name}")
        hero.health -= dam_hit
        print(f"{hero.name} is currently at {hero._health} HP")

    


main()



    
    


