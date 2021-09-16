""" Projektowanie zorientowane obiektowo, ciąg dalszy pizzeri"""

from employee import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, 'zamawia pizzę u kelnera ', server)
    def pay(self, server):
        print(self.name, 'płaci zazamówienie u kelnera ', server)

class Oven:
    def bake(self):
        print('piec piecze')

class PizzaShop:
    def __init__(self):
        self.server = Server('Krystek')
        self.chef = PizzaRobot('Robot')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Zenon')
    print('-----' * 5)
    scene.order('Aniela')
