from collections import deque

graph = {}
graph['ania'] = ['alicja', 'bartek', 'cecylia']
graph['alicja'] = ['patrycja']
graph['bartek'] = ['janusz', 'patrycja']
graph['cecylia'] = ['jarek', 'tamara']
graph['janusz'] = []
graph['tamara'] = []
graph['jarek'] = []
graph['patrycja'] = []

def person_is_seller(name):
    return name[-1] == 'z'

def search(name):
    search_que = deque()
    search_que += graph[name]
    searched = []
    while search_que:
        person = search_que.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person + ' sprzedaje mango!')
                return True
            else:
                search_que += graph[person]
                searched.append(person)
    return False

search('ania')