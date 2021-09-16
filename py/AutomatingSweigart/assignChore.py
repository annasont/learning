'''assignChore.py'''
import random, smtplib

def assignChore(chores, familyMembers):
    for member in familyMembers:
        familyMembers[member]['chores'] = []

    while len(chores) >= len(familyMembers):
        for member in familyMembers:
            randomChore = random.choice(chores)
            familyMembers[member]['chores'].append(randomChore)
            chores.remove(randomChore)

    while len(chores) > 0:
        allMembers = list(familyMembers.keys())
        randomMember = random.choice(allMembers)
        randomChore = random.choice(chores)
        familyMembers[randomMember]['chores'].append(randomChore)
        chores.remove(randomChore)
        allMembers.remove(randomMember)

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    print('Enter password:')
    password = input()
    smtpObj.login('aniasontowska@gmail.com', password)

    for member in familyMembers:
        memberChores = ', '.join(familyMembers[member]['chores'])
        email = familyMembers[member]['email']
        message = 'Subject: Domowe obowiazki\nCzesc %s\n\nW tym tygodniu wylosowales/wylosowalas nastepujace obowiazki: %s.\n\nBuziaczki!' % (member, memberChores)
        sendMailStatus = smtpObj.sendmail('aniasontowska@gmail.com', email, message)
        if sendMailStatus != {}:
            print('There was a problem sending email to %s: %s' % (email, sendMailStatus))
        else: 
            print('Email sendt to %s' % member)

    smtpObj.quit()

if __name__ == '__main__':
    chores = ['odkurzanie', 'mycie lazienki', 'mycie kuchni', 'zakupy', 'obiad']
    familyMembers = {}
    familyMembers.setdefault('Ania', {})
    familyMembers.setdefault('Marcin', {})
    familyMembers['Ania']['email'] = 'aniasontowska@gmail.com'
    familyMembers['Marcin']['email'] = 'enclave.pevik@gmail.com'

    print(assignChore(chores, familyMembers))

