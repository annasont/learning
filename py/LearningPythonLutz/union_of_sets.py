"Część wspólna"

# dla 2 sekwencji

def intersection(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

a = (1, 2, 3, 4)
b = (3, 9, 10, 4)
c = (3, 4)

print(intersection(a, b))

# dla dowolnej liczby sekwencji

def intersection2(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if not x in other:
                break
            else:
                res.append(x)
    return res

print(intersection2(a, b, c))


# co najmniej w jednej z sekwencji:
def intersection3(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x in other:
                if not x in res:
                    res.append(x)
    return res

print(intersection3(a, b, c))


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

print(union(a, b, c))




