''' Printing lists in tables'''


myList = [['red', 'green', 'blue', 'purple'],
        ['black', 'yellow', 'white', 'brown'],
        ['pink', 'orange', 'green', 'yellow'],
        ['one', 'two', 'three', 'four'],]


def printTable(table):
    for item in range(len(table[0])):
        for line in range(len(table)):
            print((table[line][item]).rjust(10), end='  ')
        print('\n')


if __name__ == '__main__':
    print(printTable(myList))


