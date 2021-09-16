'''Phone number and email extractor
'''
import re, pyperclip
tekst = pyperclip.paste()

tekst = 'jakis tam tekst +49 111 111 111, inny mumer to 22 222 222 222, a jeszcze inny numer to 33 333333333, a ostatni to 444444444 oraz 555 555 555. Moj adres mail to anIa24sontowska@gmail.com. Mam tez inne adresy. Np. ania.Sontowska@o2.pl i ole@com.'

def findPhonenumber(tekst):
    findPhNb = re.compile(r'''(
        (\+?    # plus
        \d{2}   # kierunkowy
        \s?)?   # spacja między kierunkowym a numerem
        (\d{3}  # pierwsza tójka
        \s?     # spacja między trójkami
        \d{3}   # druga trójka
        \s?     # spacja między trójkami
        \d{3})  # trzecia trójka
    )''', re.VERBOSE)
    
    x = re.findall(findPhNb, tekst)
    res = ''
    for i in range(len(x)):
        res += x[i][0] + '\n'
    return res

def findEmail(tekst):
    findEm = re.compile(r'''(
        [a-zA-Z0-9.-_+]+        # username 
        @                       # @
        [a-zA-Z0-9]+            # domain
        (\.[a-zA-Z]{2,4})       # dot, country
    )''', re.VERBOSE | re.IGNORECASE)

    x = re.findall(findEm, tekst)
    res = ''
    for i in range(len(x)):
        res += x[i][0] + '\n'
    return res

if findPhonenumber(tekst):
    numbers = findPhonenumber(tekst)
else:
    numbers = 'No phone numbers in document'

if findEmail(tekst):
    emails = findEmail(tekst)
else:
    emails = 'No email adresses in document'

result = "Phone numbers:\n%s\nE-mails:\n%s" % (numbers, emails)

pyperclip.copy(result)
print('Numbers and addresses copied to clipboard')

print(pyperclip.paste())