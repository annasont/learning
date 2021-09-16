from person import Person, Manager

anna = Person('Anna Pierwsza', job='programmer', pay=100000)
rob = Person('Rob Poor', 0)
tom = Manager('Tom Hardy', 50000)

import shelve
db = shelve.open('persondb')
for object in (anna, rob, tom):
    db[object.name] = object
db.close()