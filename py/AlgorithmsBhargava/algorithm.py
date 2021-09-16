import collections

# recurrency
def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])

def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])

def max(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        subMax = max(arr[1:])
    if arr[0] > subMax:
        return arr[0]
    else:
        return subMax


def quicksort(arr):
    if len(arr) == 0 or len((arr)) == 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# breadth-first search
friends = {}
friends['ja'] = ['Stefan', 'Marian', 'Krystyna', 'Barbara']
friends['Marian'] = ['Karol']
friends['Krystyna'] = ['Zbyszek', 'Grzegorz']
friends['Barbara'] = ['Ela', 'Mirek']
friends['Ela'] = ['Lutek']
friends['Stefan'] = []
friends['Grzegorz'] = []
friends['Mirek'] = []
friends['Lutek'] = []
friends['Karol'] = []
friends['Zbyszek'] = []
 
def findGivenLen(length, string):
    if len(string) == length:
        return True
    return False

def search(graph, name, function, *args):
    find_person_queue = collections.deque()
    find_person_queue += graph[name]
    checked = []
    while find_person_queue:
        if find_person_queue[0] not in checked:
            if function(*args, find_person_queue[0]) == True:
                print('found it!: {}'.format(find_person_queue[0]))
                return True
            else:
                find_person_queue += graph[find_person_queue[0]]
                find_person_queue.popleft()
        else:
            find_person_queue.popleft()
    return False


print(search(friends, 'ja', findGivenLen, 5))   
    

# arr = [1, 34, 3, 10, 1, 63, 1, 12, 300, 25, 12]
# # print(sum(arr))
# # print(count(arr))
# print(quicksort(arr))


