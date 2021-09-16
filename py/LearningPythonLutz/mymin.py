"Moja funkcja minimum oraz minmax"

def mymin(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res
        

a = 12
b = 10
c = 7

print(mymin(a, b, c))

def mymin2(first, *args):
    for arg in args:
        if arg < first:
            first = arg
    return first

print(mymin2(a, b, c))

def mymin3(*args):
    temp = list(args)
    temp.sort()
    return temp[0]

print(mymin3(a, b, c))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y):
    return x < y

def grtrthan(x, y):
    return x > y


print(minmax(lessthan, a, b, c))
print(minmax(grtrthan, a, b, c))


expression = input("Type a function: ")
def minmax2(expression, *args):
    res = args[0]
    for arg in args[1:]:
        if expression == 'less':
            eval('lessthan(arg, res)')
            res = arg
        elif expression == 'grtr':
            eval('grtrthan(arg, res)')
        else:
            res = 'Wrong function.'
            break
    return res

print(minmax2(expression, a, b, c))