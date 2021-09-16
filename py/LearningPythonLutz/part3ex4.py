"Python wprowadzenie, Mark Lutz"
"Ćwiczenia do części trzeciej, zadanie 4"
L = [2 ** x for x in range(7)]
X = 5


if 2 ** X in L:
    print('pod indeksem ', L.index(2 ** X))
else:
    print('nie odnaleziono')


for i in L:
    if 2 ** X == L[L.index(i)]:
        print('pod indeksem ', L.index(i))
        break
else:
    print('nie odnaleziono')
    

for i in L:
    if 2 ** X == L[L.index(i)]:
        print('pod indeksem ', L.index(i))
        break
else:
    print('nie odnaleziono')
    
    

i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('pod indeksem ', i)
        break
    else:
        i = i + 1
else:
    print(X, 'nie odnaleziono')



for (a, b) in enumerate(L):
    if b ==  2 ** X:
        print('pod indeksem ', a)
        break     
else:
    print('Nie odnaleziono')




