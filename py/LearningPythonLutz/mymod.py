def countLines(name):
    f = open("%s.py" % name.__name__)
    return len(f.readlines())

def countChars(name):
    f = open("%s.py" % name.__name__)
    return len(f.read())

def test(name):
    lines = countLines(name)
    chars = countChars(name)
    return 'Document %s has %d lines and %d characters' % (name.__name__, lines, chars)

if __name__ == '__main__':
    import mymod
    print(test(mymod))

