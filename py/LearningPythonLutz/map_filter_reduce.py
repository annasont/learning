"lambda w map:"

L = [1, 2, 3, 4]
def update(x):
    return x + 1

print(list(map(update, L)))

print(list(map((lambda x: x + 1), L)))

L2 = [10, 9, 8, 7]



"my map:"

def mymap(funct, seq):
    res = []
    for x in seq:
        res.append(funct(x))
    return res

print(mymap(update, L2))



"wbudowane map z funkcją przymującą 2 argumenty"

print(list(map(pow, L, L2)))



"funkcja wbudowana filter"
L3 = [10, 7, 5, 3, 1, 9, 13]
 
def morethan5(x):
     return x > 5

print(list(filter(morethan5, L3)))



"my filter"

def myfilter(funct2, seq2):
    res = []
    for x in seq2:
        if funct2(x) == True:
            res.append(x)
    return res

print(myfilter(morethan5, L3))



"wbudowana funkcja reduce"
def plus(x, y):
    return x + y

def multiply(x, y):
    return x * y

import functools
print(functools.reduce(plus, L))

# trzeci, opcjonalny argument. Albo inicjuje, albo jako wartosc zastepujaca pustą listę
print(functools.reduce(plus, L, 10))



"my reduce"

def myreduce(funct3, seq3):
    res = seq3[0]
    for x in seq3[1:]:
        res = funct3(res, x)
    return res

print(myreduce(plus, L))
print(myreduce(multiply, L))


