d = {'a':1, 'b':2, 'c':3}
d2 = {'a':10, 'y':20, 'z':30}

# wbudowane metody copy oraz łączenie słowników:
# dcopy = d.copy()
# d.update(d2)
# print(dcopy)
# print(d)

l = [1, 2, 3]
l2 = [10, 20, 30]


'kopia słownika' 

def copyDict(dict):
    keylist = dict.keys()
    newD = {}
    for key in keylist:
        newD[key] = dict[key]
    return newD

def copyDict2(dict1, dict2):
    keylist1 = dict1.keys()
    keylist2 = dict2.keys()
    newD = {}
    for key in keylist1:
        newD[key] = dict1[key]
    for key in keylist2:
        newD[key] = dict2[key]
    return newD

print(copyDict2(d, d2))

def copydictorlist(arg1, arg2):
    if type(arg1) == dict:
        keylist1 = arg1.keys()
        keylist2 = arg2.keys()
        copy = {}
        for key in keylist1:
            copy[key] = arg1[key]
        for key in keylist2:
            copy[key] = arg2[key]
    if type(arg1) == list:
        copy = []
        for i in (arg1 + arg2):
            copy.append(i)
    return copy

print(copydictorlist(d, d2))
print(copydictorlist(l, l2))



