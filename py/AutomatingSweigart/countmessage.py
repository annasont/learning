""" countmessage.py gives number of characters in a message.
"""
message = 'Some message with a lot of letters and so on.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

for x in sorted(count.keys()):
    print('%s => %s' % (x, count[x]))
 



