"""Object-oriented programming. zoo as an example"""
class Animal:
    def reply(self):
        self.speak()
    def speak(self):
        print ('zwierze')


class Mammal(Animal):
    def speak(self):
        print ('ssak')

class Cat(Mammal):
    def speak(self):
        print ('miau')

class Dog(Mammal):
    def speak(self):
        print ('hau')

class Primate(Mammal):
    def speak(self):
        print ('naczelny')

class Hacker(Primate):
    def speak(self):
        print ('hello, world')

if __name__ == '__main__':
    spot = Animal()
    spot2 = Mammal()
    spot3 = Hacker()
    print(spot3.reply())
    print(spot2.reply())






