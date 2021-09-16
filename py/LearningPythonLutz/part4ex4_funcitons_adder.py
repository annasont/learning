"Python wprowadzenie, Mark Lutz"

from functools import reduce


def adder1(*args):
    print('first function adder: ', end='')
    sum = args[0]
    for arg in args[1:]:
        sum += arg
    return sum

def adder2(*args):
    print('second function adder: ', end='')
    return reduce((lambda x, y: x + y), args)

'cwiczenie ze slowami kluczowymi'

def adderkey1(*args, good='good', bad='bad', ugly='ugly'):
    keyargs = [good, bad, ugly]
    otherargs = list(args)
    args = keyargs + otherargs
    sum = args[0]
    for arg in args[1:]:
        sum += arg
    return sum

def adderkey2(*args, good=1, bad=2, ugly=3):
    keyargs = [good, bad, ugly]
    otherargs = list(args)
    args = keyargs + otherargs
    return reduce((lambda x, y: x + y), args)

def adderkey3(**args):
    keyargs = list(args.values())
    sum = keyargs[0]
    for arg in keyargs[1:]:
        sum += arg
    return sum

def adderkey4(**args):
    keyargs = list(args.keys())
    sum = args[keyargs[0]]
    for key in keyargs[1:]:
        sum += args[key]
    return sum

        


print(adder1(3, 4, 7))
print(adder2(3, 4, 7))
print(adderkey1(10, 15, good=1, bad=2, ugly=3))
print(adderkey2(10, 15, good=1, bad=2, ugly=3))
print(adderkey3(good=1, bad=2, ugly=3))
print(adderkey4(good=1, bad=2, ugly=3))