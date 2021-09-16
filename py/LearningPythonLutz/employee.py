"""Object-oriented programming. Pizza shop as an example."""

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def work(self):
        print(self.name, 'Robi różne rzeczy')
    def GiveRaise(self, percent):
        self.salary += (self.salary * percent)
    def __repr__(self):
        return "Pracownik: imię = %s, wynagrodzenie = %s" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=5000)
    def work(self):
        print(self.name, 'przygotowuje jedzenie')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=4000)
    def work(self):
        print(self.name, 'obsługuje klienta')

class PizzaRobot(Chef):
    def work(self):
        print(self.name, 'przygotowuje pizzę')

if __name__ == '__main__':
    jeff = PizzaRobot('Jeff')
    print(jeff)
    jeff.work()
    jeff.GiveRaise(.20)
    print(jeff)

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
