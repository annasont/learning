"""
Quizgenarator: Program that generates 35 quizes (with keys) with European countries and their capitals.
Questions and answers are in random order.
"""
import random

capitals = {'Albania': 'Tirana',
            'Andorra': 'Andorra la Vella',
            'Armenia': 'Yerevan',
            'Austria': 'Vienna',
            'Azerbaijan': 'Baku',
            'Belarus': 'Minsk',
            'Belgium': 'Brussels',
            'Bosnia and Herzegovina': 'Sarajevo',
            'Bulgaria': 'Sofia',
            'Croatia': 'Zagreb',
            'Czechia': 'Prague',
            'Cyprus': 'Nicosia',
            'Denmark': 'Copenhgen',
            'Estonia': 'Tallinn',
            'Finland': 'Helsinki',
            'France': 'Paris',
            'Georgia': 'Tibilisi',
            'Germany': 'Berlin',
            'Greece': 'Athens',
            'Hungary': 'Budapest',
            'Iceland': 'Reykjavik',
            'Ireland': 'Dublin',
            'Italy': 'Rome',
            'Kazakhstan': 'Nur-Sultan',
            'Kosovo': 'Pristina',
            'Latvia': 'Riga',
            'Lichtenstein': 'Vaduz',
            'Lithuania': 'Vilnius',
            'Luxembourg': 'Luxembourg',
            'Malta': 'Valletta',
            'Moldova': 'Chisinau',
            'Monaco': 'Monaco',
            'Montenegro': 'Podgorica',
            'Netherlands': 'Amsterdam',
            'Macedonia': 'Skopje',
            'Norway': 'Oslo',
            'Poland': 'Warsaw',
            'Portugal': 'Lisbon',
            'Romania': 'Bucharest',
            'Russia': 'Moscow',
            'San Marino': 'San Marino',
            'Serbia': 'Belgrade',
            'Slovakia': 'Bratislava',
            'Slovenia': 'Ljubljana',
            'Spain': 'Madrid',
            'Sweden': 'Stockholm',
            'Switzerland': 'Bern',
            'Turkey': 'Ankara',
            'Ukraine': 'Kyiv',
            'United Kingdom': 'London',
            'Vatican': 'Vatican City'}

for i in range(35):
    keysList = list(capitals.keys())
    random.shuffle(keysList)
    quiz = open('student%s.txt' % (i + 1), 'a')
    quizKey = open('student%skey.txt' % (i + 1), 'a')
    n = 0
    for key in keysList:
        n += 1
        answList = (list(capitals.values()))
        random.shuffle(answList)
        listWithRighAnsw = [capitals[key], answList[0], answList[1], answList[2]]
        random.shuffle(listWithRighAnsw)
        quiz.write('\n%d What is the capital of %s?\nA) %s\nB) %s\nC) %s\nD) %s\n' % (n, key, listWithRighAnsw[0], listWithRighAnsw[1], listWithRighAnsw[2], listWithRighAnsw[3]))
        quizKey.write('\n%d What is the capital of %s?\nAnswer: %s\n' % (n, key, capitals[key]))
    quiz.close()
    quizKey.close()
