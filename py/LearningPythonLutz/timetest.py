"testy pomiaru czasu dla listy"

import sys, mytimer

reps = 10000
repslist = range(reps)

# def forLoop():
#     res = []
#     for x in repslist:
#         res.append(abs(x))
#     return res

# def listComp():
#     return [abs(x) for x in repslist]

# def mapCall():
#     return list(map(abs, repslist))

# def genExpr():
#     return list((abs(x) for x in repslist))

# def genFunc():
#     def gen():
#         for x in repslist:
#             yield abs(x)
#     return list(gen())

# print(sys.version)
# for test in (forLoop, listComp, mapCall, genExpr, genFunc):
#     elapsed, result = mytimer.timer(test)
#     print('- ' * 30)
#     print('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

# "testy pomiaru czasu dla listy"

# import sys, mytimer

# reps = 10000
# repslist = range(reps)

def forLoop2():
    res = []
    for x in repslist:
        res.append(x * 3)
    return res

def listComp2():
    return [x * 3 for x in repslist]

def mapCall2():
    return list(map(lambda x: x * 3, repslist))

def genExpr2():
    return list((x * 3 for x in repslist))

def genFunc2():
    def gen():
        for x in repslist:
            yield x * 3
    return list(gen())


# print(sys.version)
# for test in (forLoop2, listComp2, mapCall2, genExpr2, genFunc2):
#     elapsed, result = mytimer.timer(test)
#     print('- ' * 30)
#     print('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

print(sys.version)
for tester in (mytimer.timer, mytimer.besttime):
    for test in (forLoop2, listComp2, mapCall2, genExpr2, genFunc2):
        total, result = mytimer.timer(test)
        best, result = mytimer.besttime(test)
        print('- ' * 30)
        print('%-10stotal: %-1s %-5.5f => [%s...%s]' % (test.__name__, '', total, result[0], result[-1]))
        print('%-10sbest: %-2s %-5.5f => [%s...%s]' % (test.__name__, '', best, result[0], result[-1]))


