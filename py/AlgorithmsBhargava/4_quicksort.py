# 
def quicksort(list):
    less = []
    more = []
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        more = [i for i in list[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(more)
    

x = [1, 5, 399, 53, 29, 45, 0, 89]


print (quicksort(x))















