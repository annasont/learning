while True:
    reply = input('Wpisz tekst: ')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Niepoprawne dane')
    else:
        print(int(reply) ** 2)
print('koniec!')

