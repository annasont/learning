

def sum(list):
    if len(list) == 1:
        return list[0]
    else: 
        return list.pop(0) + sum(list)
        

print (sum([2, 4, 6]))

x = [3, 8, 1, 2]
print (sum(x))


def sum2(list):
    if list == []:
        return 0
    else:
        return list[0] + sum2(list[1:])


z = [1, 2, 3]
print (sum2(z))

