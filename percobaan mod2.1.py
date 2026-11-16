class hero:
    
    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        self.__private = "private"
        self.__protected = "protected"

hero_1 = hero('Atsu', 100)

print(hero_1.__dict__)
print(hero.__dict__)
print(hero._hero__privatejumlah)
