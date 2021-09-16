file = open('saveit.txt').readlines()

lines = [line.rstrip() for line in file]
print(lines)

print(list(map(lambda line: line.rstrip(), file)))

listoftuples = [('Ania', 30, 'czerwiec'), ('Marcin', 32, 'maj')]

imiona = [listoftuples[i][0] for i in range(len(listoftuples))]
print(imiona)

imiona2 = [name for (name, age, month) in listoftuples]
print(imiona2)


def name(list):
    return list[0]

print(list(map(name, listoftuples)))

print(list(map((lambda list: list[0]), listoftuples)))

res = []
for x in range(len(listoftuples)):
    res.append(listoftuples[x][2])
print(res)