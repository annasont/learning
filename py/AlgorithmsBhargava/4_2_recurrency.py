
def length(list):
    
    if len(list) == 0:
        return 0
    else:
        list.pop()
        return 1 + length(list)
        
x = [3, 5, 7]

print (length(x))

y = [2, 4, 5, 4, 3]

def length2(list):

    if list == []:
        return 0
    else:
        return 1 + length2(list[1:])

print (length2(y))