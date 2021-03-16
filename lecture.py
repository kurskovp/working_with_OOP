
#и сразу реализуем множественное наследрвание!

class Character():
    name = ''
    power =0
    energy = 100
    hands = 2

class Spider():
    power = 0
    energy = 50
    hands = 8

    def webshoot(self):
        print('Pew-Pew!')

class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        self.name = name
        self.power = power


peter_parker = SpiderMan('Peter Parker', 80)
print(peter_parker.name)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)
peter_parker.webshoot()

print(SpiderMan.mro())