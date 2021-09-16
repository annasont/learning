import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key, '=>', db[key])

anna = db['Anna Pierwsza']
anna.giveRaise(.15)
db['Anna Pierwsza'] = anna
db.close()
