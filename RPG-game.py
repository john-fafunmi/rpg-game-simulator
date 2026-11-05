class Hero:

    def __init__(self, name):
        self.name = name
        self._health = 100
        self._level = 0

    def __str__(self):
        return f"Hero Name: {self.name}\nHero Health: {self._health}\nHero Level: {self._level}"
    
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
    @property
    def level(self):
        return self._level
    @level.setter
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
        self.level = 1

    def __str__(self):
        return f"Monster Name: {self.name}\nMonster Health: {self._health}\nMonster Level: {self.level}"
lol = Hero("John")
mon = Monster("Gargoyle")




    
    


