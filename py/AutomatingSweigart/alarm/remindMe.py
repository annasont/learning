'''remindMe.py checks e-mails from last 24 hours, if finds e-mails from given adress with subject "wake up",
activates alarm and prints body text to txt file and opens it. Deletes email afterwards. 
Use f.eks. scheduler to ran program every xx minutes'''
import sys, imapclient, pyzmail, datetime, subprocess, traceback

if len(sys.argv) > 1:
    password = sys.argv[1]
else:
    print('Password missing.')

oneDay = datetime.timedelta(days=1)
oneDayAgo = datetime.datetime.now() - oneDay
oneDayAgoFormated = oneDayAgo.strftime('%d-%b-%Y')

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('aniasontowska@gmail.com', password)
imapObj.select_folder('INBOX', readonly=False)
IDs = imapObj.search(['FROM', 'aniasontowska@gmail.com', 'SINCE', oneDayAgoFormated])
rawMessages = imapObj.fetch(IDs, ['BODY[]'])

try:
    for item in IDs:
        message = pyzmail.PyzMessage.factory(rawMessages[item][b'BODY[]'])
        if message.get_subject() == "wake up" or message.get_subject() == "wakeup":
            subprocess.Popen(['xdg-open', 'alarm.wav'])
            if message.text_part != None:
                bodyText = message.text_part.get_payload().decode(message.text_part.charset)
                messageFile = open('messageFile.txt', 'w')
                messageFile.write(bodyText)
                messageFile.close
                subprocess.Popen(['xdg-open', 'messageFile.txt'])
            imapObj.delete_messages(item)
            imapObj.expunge()
except:
    errorFile = open('errorFile.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()

#check: empty message file