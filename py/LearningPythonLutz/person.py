from classtools import AttrDisplay

class Person(AttrDisplay):
    "Tworzy i przetwarza rekordy osób"
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def lastName(self):
        return self.name.split()[-1]

class Manager(Person):
    "Klasa podrzędna. Dostosowana do potrzeb klasa 'Person': Nadpisanie def giveRaise"
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

class Department:
    "Osadzanie obiektów w kompozytach. Agregowanie obiektów w celu potraktowania ich jako zbiór"
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

if __name__ == "__main__":
    anna = Person('Anna Pierwsza', job='programmer', pay=100000)
    rob = Person('Rob Poor', 0)
    tom = Manager('Tom Hardy', 50000)
    for object in (anna, rob, tom):
        object.giveRaise(.10)
        print(object.pay)

    print(anna)

    # development = Department(anna, rob)
    # development.addMember(tom)
    # development.giveRaises(.20)
    # for object in (anna, rob, tom):
    #     print(object.pay)

    

