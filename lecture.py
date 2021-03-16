
#и сразу реализуем множественное наследрвание!

class Character():
  # перенесём всё в init, т.к. теперь мы сможем его наследовать при помощи функции super()
    def __init__(self, name, power, energy = 100, hands = 2):
        self.name = name
        self.power = power
        self.energu = energy
        self.hands = hands

class Spider():
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energu = energy
        self.hands = hands

    def webshoot(self):
        print('Pew-Pew!')

class SpiderMan(Character, Spider):
     def __init__(self, name, power):
        # мы можем полностью унаследовать init родителя и до super().__init__(name,power)
         super().__init__(name,power)
         self.backpack = []   # добавили рюкзак


     def attack(self):
        # если в рюкзаке имеется паутина тогда стреляй по стрельбе взятой от родителя
        # через функцию super()
         if 'web' in self.backpack:
            super().webshoot()
         else:
            print('No web!')

peter_parker = SpiderMan('Peter Parker', 80)
# print(peter_parker.name)
# print(peter_parker.power)
# print(peter_parker.energy)
# print(peter_parker.hands)
# peter_parker.webshoot()
peter_parker.attack()
peter_parker.backpack.append('web')
peter_parker.attack()

print(SpiderMan.mro())