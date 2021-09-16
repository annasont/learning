# 
def highestNumber(list):
    
    if len(list) == 1:
        return list[0]
    elif list[0] >= list[1]:
        del list[1]
        return highestNumber(list)
    else:
        del list[0]
        return highestNumber(list)
        
x = [67, 736, 14, 654]

print (highestNumber(x))

y = [3, 7, 312, 29, 7, 8, 65, 22, 11, 24]

def max(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    else:
        sub_max = max(list[1:])
    if list[0] > sub_max:
        return list[0]
    else: 
        return sub_max

print (max(y))



